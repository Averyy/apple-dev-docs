# Composing dynamic sessions with instructions and profiles

**Framework**: Foundation Models

Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.

#### Overview

As you build features for sophisticated use cases, effective context management becomes essential. For example, a cooking app that provides a guided multi-step workflow where a person discovers a recipe, substitutes ingredients, searches inventory, and provides step-by-step cooking guidance. All of these steps together would be difficult to build well with a static session.

By default, a language model session evaluates instructions upon initialization, and they remain static for the session. The dynamic profiles API allows you to build your app so a session uses only what’s necessary based on the state of your app. When the context of your app changes, the instructions, tools, and model configuration change with it.

The framework introduces three composable layers for building dynamic apps that interact with language models:

- ****Dynamic instructions****: Re-evaluate before every model request and supply the instructions and tools needed at that time.
- ****Profiles****: Associate dynamic instructions with session-level properties, like which model to use and the reasoning level.
- ****Dynamic profiles****: Orchestrates transitions between multiple profiles and maintains one active profile at a time.

Because the body of dynamic instructions re-evaluates before each call to the model, the model always sees a snapshot of your app’s current state.

#### Declare Dynamic Instructions

You use [`DynamicInstructions`](dynamicinstructions.md) to declaratively specify the instructions and list of tools that are necessary for the state your app is in. Conform a type to [`DynamicInstructions`](dynamicinstructions.md) and implement its `body` property. Carefully consider using only the instructions and tools that are necessary for the task since a dynamic instruction evaluates before each model request.

In the `body` of your type, include any [`Instructions`](instructions.md) block, [`Tool`](tool.md) instances, and nested [`DynamicInstructions`](dynamicinstructions.md). Because the `body` of your type evaluates before each model request, add any necessary conditionals to load or exclude items based on your runtime state.

```swift
struct PresentationInstructions: DynamicInstructions {
    // The data source for conditional instructions.
    var isEditingImage = true
    var isEditingAnimation = false

    var body: some DynamicInstructions {
        // The instructions and tools that remain the same across any use of this type.
        Instructions {
            "Help people improve their presentation."
        }
        ListPhotosTool()
        AddPhotoTool()

        // Depending on the state of the app, include additional instructions
        // that provide the model with more task-specific instructions and tools.
        if isEditingImage {
            ImageEditingInstructions()
        }
        
        if isEditingAnimation {
            AnimationEditingInstructions()
        }
    }
}
```

Because the `body` re-evaluates before every model request, switching from image editing to animation editing automatically updates the active toolset.

Nest [`DynamicInstructions`](dynamicinstructions.md) conformances to keep each concern self-contained. The custom `ImageEditingInstructions` type above, for example, bundles its own instructions and tools for use across different parts of the app.

After declaring your [`DynamicInstructions`](dynamicinstructions.md), pass them to [`LanguageModelSession`](languagemodelsession.md) using the [`init(model:dynamicInstructions:history:)`](languagemodelsession/init(model:dynamicinstructions:history:).md) initializer:

```swift
let session = LanguageModelSession(
    dynamicInstructions: PresentationInstructions()
)
```

> ❗ **Important**: When conditionally providing instructions and tools, append them in place to improve latency from the use of model caching. For more information about prompt caching, see [`Optimizing key-value caching in language model sessions`](optimizing-key-value-caching-in-language-model-sessions.md).

#### Configure a Profile

A [`LanguageModelSession.Profile`](languagemodelsession/profile.md) associates [`DynamicInstructions`](dynamicinstructions.md) with session-level properties, making instructions, tools, and modifiers more dynamic. Compose a [`LanguageModelSession.Profile`](languagemodelsession/profile.md) based on the task you want to accomplish. Parameterizing instructions, tools, and modifiers makes the API surface flexible enough to fit your needs. For example, you might choose to parameterize the model temperature and reasoning level depending on the state of your app:

```swift
Profile {
    // Custom instructions and tools for a creative task. 
}
// Use an instance of the PCC model you create in the parent profile.
.model(pccModel)
// Use a higher creative temperature value when a person likes poetry.
.temperature(likesPoetry ? 0.8 : 0.1)
// Perform deeper reasoning when a person likes astronomy.
.reasoningLevel(likesAstronomy ? .deep : .light)
```

#### Orchestrate Multiple Profiles with a Dynamic Profile

Instead of writing an all-encompassing profile, break up the problem into multiple domain-specific profiles. A [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) orchestrates the transitions between your profiles by using conditionals and nesting. When the active profile changes, the session adopts the new model and generation options on the next model request. The following diagram illustrates a dynamic profile managing three profiles, each with their own model configuration and conditional instructions:

![A diagram that illustrates a dynamic profile that manages three profiles. There](https://docs-assets.developer.apple.com/published/2be58f2539b63b598108e060ec47dca9/composing-dynamic-sessions-with-instructions-and-profiles-dynamic-profile%402x.png)

A [`LanguageModelSession.DynamicProfileBuilder`](languagemodelsession/dynamicprofilebuilder.md) enforces a hard constraint at compile time so exactly one [`LanguageModelSession.Profile`](languagemodelsession/profile.md) is active at a time. Instead of using parallel `if` blocks, use expressions so the compiler verifies the constraint:

```swift
struct PresentationProfile: LanguageModelSession.DynamicProfile {
    // Create an instance to the server model.
    var pccModel = PrivateCloudComputeLanguageModel()
    
    // The data source for the profile.
    var isEditingImage = true
    var isEditingAnimation = false

    // Determine which profile to load based on the current state.
    var body: some LanguageModelSession.DynamicProfile {
        if isEditingImage {
            Profile {
                ImageEditingInstructions()
            }
        } else if isEditingAnimation {
            Profile {
                AnimationEditingInstructions()
            }
            .model(pccModel)
            .temperature(0.2)
            .reasoningLevel(.light)
        } else {
            Profile {
                PresentationDynamicInstructions()
            }
            .temperature(0.8)
        }
    }
}
```

Pass the dynamic profile to [`LanguageModelSession`](languagemodelsession.md) using the [`init(profile:history:)`](languagemodelsession/init(profile:history:).md) initializer:

```swift
let session = LanguageModelSession(
    profile: PresentationProfile()
)
```

#### Apply Modifier Precedence Rules

Dynamic profiles and subprofiles support the same value modifiers, like temperature, reasoning level, and so on. When the same modifier appears at multiple levels, a three-tier precedence rule determines which value to use — from highest to lowest priority:

1. **Call-site arguments** — Generation options you pass directly to `respond(to:options:)` override all profile and dynamic profile modifiers.
2. **Innermost dynamic profile or profile modifier** — The modifier closest to the subprofile declaration overrides a dynamic profile.
3. **Dynamic profile modifiers** — Act as defaults that apply to all subprofiles unless the modifier is overridden by a subprofile.

Use profile modifiers to establish baseline defaults, then let individual subprofiles refine or override them:

```swift
// A top-level dynamic profile that includes a single subprofile.
struct WritingProfile: LanguageModelSession.DynamicProfile {
    var body: some LanguageModelSession.DynamicProfile {
        // By default, the temperature value applies to both branches in 
        // `WritingContent` unless a branch adds a temperature modifier.
        WritingContent()
            .temperature(0.5)
    }
}

// A dynamic profile that contains two states.
struct WritingContent: LanguageModelSession.DynamicProfile {
    // A custom writing mode that determines which subprofile to use.
    var mode: MyCustomWritingMode = .creative

    var body: some LanguageModelSession.DynamicProfile {
        switch mode {
        case .creative:
            // Use the temperature `1.0` because the profile-level modifier takes priority.
            Profile {
                CreativeWritingInstructions()
            }
            .temperature(1.0)  
        case .technical:
            // Inherit the temperature `0.5` from `WritingProfile`.
            Profile {
                TechnicalWritingInstructions()
            }
        }
    }
}
```

#### Respond to Life Cycle Events

Observe and react to key moments during a session by using life cycle modifiers. Unlike value modifiers, life cycle callbacks accumulate across nested profiles. When a profile and a subprofile both register a callback, the framework calls both. The following shows the available modifiers and when they run:

| Modifier | Description |
| --- | --- |
| [`onActivate(perform:)`](languagemodelsession/dynamicprofile/onactivate(perform:).md) | Runs when the profile becomes active and allows for set up work. |
| [`onDeactivate(perform:)`](languagemodelsession/dynamicprofile/ondeactivate(perform:).md) | Runs when the profile becomes inactive and allows for teardown work. |
| [`onPrompt(perform:)`](languagemodelsession/dynamicprofile/onprompt(perform:).md) | Runs after the user prompt appends to the transcript, but before the model request starts. |
| [`onResponse(perform:)`](languagemodelsession/dynamicprofile/onresponse(perform:).md) | Runs after the model produces a response. |
| [`onToolCall(perform:)`](languagemodelsession/dynamicprofile/ontoolcall(perform:).md) | Runs when the model invokes a tool. |
| [`onToolOutput(perform:)`](languagemodelsession/dynamicprofile/ontooloutput(perform:).md) | Runs when a tool call produces output. |

Use life cycle events as validation checkpoints by throwing an error. Throwing an error inside a life cycle callback propagates to the caller’s [`respond(to:options:)`](languagemodelsession/respond(to:options:).md) or [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:).md) call, letting you raise errors that surface directly to your call site:

```swift
Profile {
    MyCustomFileAccessInstructions()
    MyCustomReadFileTool()
}
.onToolCall { toolCall in
    // Runs before the framework invokes the tool and allows for checking 
    // whether the app is in a state to run the tool.
    guard myAccessPolicy.permits(toolCall) else {
        throw MyAccessPolicyError.denied(toolCall.toolName)
    }
}
.onToolOutput { toolCall, output in
    // Runs after the tool. This is a good place to log any necessary activity.
}
```

#### Access Session Level Properties

The building blocks of dynamic instructions and profiles help you define what the model sees and how it’s configured. Use `@SessionProperty` to access session properties from within a [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md), [`LanguageModelSession.Profile`](languagemodelsession/profile.md), [`DynamicInstructions`](dynamicinstructions.md), and [`Tool`](tool.md).

The session history provides the transcript entries after instructions such as prompts, responses, tool calls, and tool outputs. The history excludes instructions segments from `DynamicInstructions`. Accessing the history shared property gives you the ability to perform updates like compaction and summarization. Use `@SessionProperty` to access and modify transcript entries:

```swift
// Get a reference to the session history.
@SessionProperty(\.history) 
var history

var body: some LanguageModelSession.DynamicProfile {
    Profile {
        Instructions("You are a helpful assistant.")
        TodoWriteTool()
    }
    .onResponse { 
        // When the entries exceed `100`, perform a stateful update to the 
        // history so it only includes the last `50` entries.
        if history.count > 100 {
            history = history.suffix(50)
        }
    }
}
```

> **Note**: Because model output influences the evaluation of [`DynamicInstructions`](dynamicinstructions.md) and [`Tool`](tool.md), the session history is read-only in these contexts.

When you need session-scoped properties beyond the built-in history, apply the [`SessionPropertyEntry()`](sessionpropertyentry().md) macro to a stored property in an extension on [`SessionPropertyValues`](sessionpropertyvalues.md). This makes the property accessible from the components within the session when you use [`LanguageModelSession.SessionProperty`](languagemodelsession/sessionproperty.md). For example, to create a custom [`Tool`](tool.md) to access shared state, extend [`SessionPropertyValues`](sessionpropertyvalues.md) with a new property and then access it with [`LanguageModelSession.SessionProperty`](languagemodelsession/sessionproperty.md) from the tool:

```swift
extension SessionPropertyValues {
    @SessionPropertyEntry 
    var activatedSkills: [String: Bool] = [:]
}

struct PlannerTool: Tool {
    let description = "Update the state of the activated skills"
    
    // Read the shared session state for the currently activated skills.
    @SessionProperty(\.activatedSkills) 
    var activatedSkills

    @Generable
    struct Arguments {
        @Guide(description: "The skills to activate")
        var skills: [String]
    }

    func call(arguments: Arguments) -> String {
        // When the model calls this tool, update the skills to an active state.
        for skill in arguments.skills {
            activatedSkills[skill] = true
        }
        return "Activated: \(arguments.skills.joined(separator: ", "))"
    }
}
```

#### Create Reusable Components with a Custom Modifier

A [`LanguageModelSession.DynamicProfileModifier`](languagemodelsession/dynamicprofilemodifier.md) allows you to compose traits like model selection, temperature, life cycle callbacks, and so on, into a self-contained modifier that you attach to your profile. A modifier receives the wrapped content and returns a new [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) `body`. For example, the following creates a low temperature modifier for debugging that logs debug information after a request:

```swift
struct DebugProfileModifier: LanguageModelSession.DynamicProfileModifier {
    func body(content: Content) -> some LanguageModelSession.DynamicProfile {
        content
            .temperature(0.0)
            .onResponse { response in
                print("Debug response: \(response)")
            }
    }
}

extension LanguageModelSession.DynamicProfile {
    func debug() -> some LanguageModelSession.DynamicProfile {
        self.modifier(DebugProfileModifier())
    }
}
```

To use a custom modifier, apply it to your [`LanguageModelSession.Profile`](languagemodelsession/profile.md):

```swift
Profile {
    Instructions("You are a helpful assistant.")
}
.debug()
```

#### Transform the Session History

Because the transcript grows with every turn in a session, context size limits become important to consider. Before prompting the model, a profile can transform the transcript it sends to filter entries that aren’t necessary for the request. For example, you might drop completed tool calls, or even remove sensitive information, before sending a request to a model. Use the [`historyTransform(_:)`](languagemodelsession/dynamicprofile/historytransform(_:).md) modifier to receive the current history before each model request and return only the entries to use for the request. The following only sends the last twenty entries to the model:

```swift
Profile {
    Instructions("You help people generate fun and interesting book ideas.")
    MyCustomBookTool()
}
.historyTransform { history in
    // Perform a local transformation before prompting the model. This transform
    // doesn't affect the global state of the transcript, so you're not losing
    // existing transcript context.
    Array(history.suffix(20))
}
```

When a [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) coordinates multiple profiles, [`historyTransform(_:)`](languagemodelsession/dynamicprofile/historytransform(_:).md) allows each profile to manage its own view of the history. One profile compresses the history for a small on-device model, and a profile that uses a server model — with a much larger context size — gets the full history.

## See Also

- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [struct DynamicInstructionsForEach](dynamicinstructionsforeach.md)
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/composing-dynamic-sessions-with-instructions-and-profiles)*