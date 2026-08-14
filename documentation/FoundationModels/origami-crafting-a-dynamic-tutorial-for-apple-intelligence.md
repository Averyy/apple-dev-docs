# Origami: Crafting a dynamic tutorial for Apple Intelligence

**Framework**: Foundation Models

Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Picking up a new craft can be time-consuming, and the Origami app eases you into the art of folding paper into intricate shapes using an easy-to-follow tutorial as your guide. But it’s not just about folding paper; you can use Origami to learn any craft you can make from supplies you have on hand, like crocheting, knitting, or sewing.

![A screenshot of the Origami app’s Brainstorm view showing the person’s supply photos alongside generated craft-project ideas.](/images/com.apple.foundationmodels/origami-hero@2x.png)

You start by providing a photograph or two of your supplies or inspiration and asking Origami what you can make from them. Origami responds with craft project ideas. You then pick one of the suggested projects, follow a tutorial, and photograph your work at each step so the app can coach you.

Those two interactions rely on multimodal prompting: *Brainstorm* turns photos of your supplies or inspiration into project ideas, and *Coach* compares a progress photo to the current step and tells you how you’re doing as you work through a tutorial.

Brainstorm and Coach use [`LanguageModelSession`](languagemodelsession.md) to accept images and text. You attach a [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage) to a [`Prompt`](prompt.md), add the text that frames it, and the session returns a [`Generable`](generable.md) value you can render. The picture isn’t a side channel that feeds a separate vision step. It sits in the prompt as a peer to the text and the same model processes the two together.

#### Configure the Sample Code Project

For best performance, run Origami on device to experience Apple Intelligence and Private Cloud Compute (PCC). You need a device that supports Apple Intelligence, running iOS 27, iPadOS 27, or macOS 27 or later.

Before you build and run Origami, turn on Apple Intelligence:

- On iOS and iPadOS, open Settings > Apple Intelligence & Siri.
- On macOS, open System Settings > Apple Intelligence & Siri.

By default, Origami runs every mode on the on-device [`SystemLanguageModel`](systemlanguagemodel.md), so the project builds and runs without additional configuration. To route Brainstorm and Coach through PCC instead, see [`Adopt Private Cloud Compute`](origami-crafting-a-dynamic-tutorial-for-apple-intelligence#Adopt-Private-Cloud-Compute.md).

Origami works with images you choose from your Photos library. The project provides a folder called `Sample Photos` that contains images you can add to your library to use with the app.

#### Configure a Session for Each Task

Origami runs a single long-lived [`LanguageModelSession`](languagemodelsession.md) and switches its configuration based on what the app is doing. The sample defines three modes:

- `.brainstorm` mode runs with a high temperature, so the model produces fresh, varied ideas each time.
- `.tutorial` mode powers two things: generating the tutorial steps, and Coach checking a progress photo against the current step.
- `.term` mode runs a fast, on-device [`SystemLanguageModel`](systemlanguagemodel.md) for terminology lookups.

A [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) called `OrchestratorProfile` returns a different [`LanguageModelSession.Profile`](languagemodelsession/profile.md) for each mode. Switching modes reconfigures the session in place rather than spinning up a new one.

Each mode pairs its own instructions with a model and a different *temperature*. Temperature controls how much the model varies its responses. A higher value makes its output more varied and creative, and a lower value keeps it more focused and predictable.

The other two modes share a `serverModel` property whose initializer determines which model they use:

```swift
struct OrchestratorProfile: LanguageModelSession.DynamicProfile {
    var orchestrator: Orchestrator

    // Swap to PrivateCloudComputeLanguageModel() to opt into PCC.
    var serverModel = SystemLanguageModel()

    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .brainstorm:
            Profile {
                BrainstormInstructions(orchestrator: orchestrator)
            }
            .model(serverModel)
            .temperature(1.0)

        case .tutorial:
            if !isOnDevice {
                Profile {
                    TutorialInstructions(orchestrator: orchestrator)
                }
                .model(serverModel)
                .reasoningLevel(.deep)
            } else {
                Profile {
                    TutorialInstructions(orchestrator: orchestrator)
                }
                .model(SystemLanguageModel())
            }

        case .term:
            Profile {
                TermInstructions(orchestrator: orchestrator)
            }
            .model(SystemLanguageModel())
        }
    }

    private var isOnDevice: Bool {
        type(of: serverModel) == SystemLanguageModel.self
    }
}
```

The instructions for each mode are a [`DynamicInstructions`](dynamicinstructions.md) value, not a plain string. That lets the instructions live next to the feature that owns them and gives them access to the current `orchestrator`:

```swift
struct BrainstormInstructions: DynamicInstructions {
    let orchestrator: Orchestrator

    var body: some DynamicInstructions {
        Instructions(
            """
            Your job is to help the user explore and define their craft project.

            When the user shares photos, identify the craft type, colors, \
            materials, and any relevant details.

            Then generate craft project ideas that best fit what you see \
            and the user's request. If the user provides craft supplies, \
            be sure to incorporate them in the project idea.

            Recommend a specific craft that is just 1 component, unless the \
            user explicitly requests something more complex.

            Most importantly: offer ideas that truly reflect the user's \
            inspiration, materials, and what makes sense given the photos.
            """
        )

        origamiShapeOptions
    }
}
```

The full sample applies the same branching to `.brainstorm` and adds path-specific extras like a shortened transcript history on the on-device path.

A dynamic profile keeps mode-specific configuration in one place and out of the code that sends prompts. For more information, see [`Composing dynamic sessions with instructions and profiles`](composing-dynamic-sessions-with-instructions-and-profiles.md).

#### Adopt Private Cloud Compute

Origami runs every mode on the on-device [`SystemLanguageModel`](systemlanguagemodel.md) by default, so the project builds and runs without additional configuration. To route Brainstorm, the tutorial generator, and Coach through Private Cloud Compute (PCC) instead, swap the `serverModel` initializer in `OrchestratorProfile` to [`PrivateCloudComputeLanguageModel`](privatecloudcomputelanguagemodel.md) and add the managed PCC entitlement to your build:

```swift
var serverModel = PrivateCloudComputeLanguageModel()
```

When `serverModel` is the PCC model, `.tutorial` activates `.reasoningLevel(.deep)` for harder analyses, and Coach inherits that configuration when it reuses the tutorial profile. On device, the sample takes a simpler path and shortens transcript history to fit the smaller context window.

For PCC eligibility and details on requesting access to the managed entitlement, see [`Adding server-side intelligence with Private Cloud Compute`](adding-server-side-intelligence-with-private-cloud-compute.md).

#### Attach Photos to a Prompt

Origami uses a small pattern throughout: wrap a `UIImage` or `NSImage` in an [`Attachment`](attachment.md), give it a label, and place it in a [`Prompt`](prompt.md). `Photo.toPrompt()` does exactly that and returns a prompt that contains a single image attachment:

```swift
func toPrompt() async throws -> Prompt {
    #if canImport(UIKit)
    guard let image = UIImage(data: data) else {
        return Prompt {}
    }
    #elseif canImport(AppKit)
    guard let image = NSImage(data: data) else {
        return Prompt {}
    }
    #endif
    let idImage = Attachment(image).label(idString)
    return Prompt {
        idImage
    }
}
```

The label matters as much as the image. Here, `idString` uses `"Photo_\(id.uuidString.prefix(6))"` to set the label as a stable, per-photo identifier so each photo carries a name the model can refer to. [`label(_:)`](attachment/label(_:).md) lets the model point back to a specific photo in its structured output instead of describing pictures by position or guesswork.

> **Note**: The label needs to be a stable string that the model can quote back; it doesn’t have to be numeric or sequential.

A prompt holds more than one element, and an image attachment is a first-class member of that sequence. The `streamProjectImageAnalysis` extension on [`LanguageModelSession`](languagemodelsession.md) builds one prompt from a block of framing text followed by every unanalyzed photo, then returns a streaming structured response:

```swift
extension LanguageModelSession {
    func streamProjectImageAnalysis(_ project: Project) async throws
        -> LanguageModelSession.ResponseStream<ImageAnalysisList>
    {
        var imagePrompts: [Prompt] = []
        for photo in project.unanalyzedPhotos {
            imagePrompts.append(try await photo.toPrompt())
        }
        let prompt = Prompt {
            """
            The craft so far is: \(project.description)
            If an image contains a crafted item relevant to this craft's \
            title, treat that image as a finished piece. If an image \
            doesn't contain any craft, treat it as inspiration for an idea.
            """
            imagePrompts
        }
        return streamResponse(
            to: prompt,
            generating: ImageAnalysisList.self
        )
    }
}
```

The text and images go in together as one prompt, in one call. The framework accepts a variety of image types, handles image orientation, and provides tools for reading text and barcodes found in a picture. For more information, see [`Analyzing images with multimodal prompting`](analyzing-images-with-multimodal-prompting.md).

#### Shape the Response Into Swift Types

A multimodal prompt’s response comes back as a typed value the app renders directly. Origami marks its result types with `@Generable` and annotates fields with `@Guide` to steer the model. The analysis types tie each result back to the photo that produced it through an [`ImageReference`](imagereference.md):

```swift
@Generable
struct ImageAnalysis {
    var image: ImageReference
    var analysis: String

    @Guide(
        description:
            "What do you think the *purpose* of this photo is for the project?"
    )
    var typeOfImage: ImageCategory
}

@Generable
struct ImageAnalysisList {
    var images: [ImageAnalysis]
}

@Generable
struct BrainstormIdeaList {
    @Guide(.minimumCount(3))
    var ideas: [BrainstormIdea]
}
```

The [`ImageReference`](imagereference.md) field closes the loop. Its [`attachmentLabel`](imagereference/attachmentlabel.md) matches the stable label set in `toPrompt()`, so the schema expresses a relationship; this analysis belongs to that photo. The input picture and the output structure stay connected by name. A `@Guide(.minimumCount(3))` on `ideas` asks the model for at least three results, and the `ImageCategory` enumeration gives the model a fixed set of purposes to choose from:

```swift
@Generable
enum ImageCategory: String, Codable {
    case craftInspiration = "inspiration for the craft"
    case craftSupplies = "craft supplies"
    case finishedPiece = "a finished craft piece"
}
```

Describing the output as types lets the model fill in a structure instead of providing freeform text. For more information, see [`Generating Swift data structures with guided generation`](generating-swift-data-structures-with-guided-generation.md).

#### Generate Ideas From Inspiration Photos

Brainstorm runs two passes on the same session. The first pass is `streamProjectImageAnalysis`, which classifies each photo into the session’s context and streams back an `ImageAnalysisList`. Because that call places the photos into the session’s transcript, the model has already seen them by the time the second pass runs. The second pass asks for ideas with a short, text-only prompt:

```swift
let stream = session.streamResponse(
    to: "What can I make with this? Please offer 3 ideas.",
    generating: BrainstormIdeaList.self
)
try await brainstorm.processStream(stream)
```

The phrase “with this” refers to images the session already holds, so the idea prompt carries no attachments of its own. Splitting the work into an analysis pass and an idea pass keeps each prompt focused, and the session’s memory of the photos ties the two together.

#### Coach Progress From a Photo

In Origami, Coach is built from two pieces working together:

- The response streams back as plain text that the UI renders as it arrives.
- A `MovePhotoToStepTool` tool call advances the tutorial when the model determines the step is complete. For more on tool calls, see [`Expanding generation with tool calling`](expanding-generation-with-tool-calling.md).

The walkthrough that follows takes a different approach by encapsulating the entire response as a structured `@Generable` value with a Boolean classifier field. Both approaches work; the choice depends on whether you want free-form prose or schema-shaped output.

![A screenshot of Coach reading the person’s progress photo and showing structured feedback alongside the current tutorial step’s instructions.](/images/com.apple.foundationmodels/origami-coach@2x.png)

In this approach, Coach sends the same kind of multimodal prompt as Brainstorm, aimed at a different question: whether the person’s latest progress photo matches what the current tutorial step asks for. The prompt, which uses the same `toPrompt()` idiom Brainstorm uses, builds from the step number, the step’s text, an instruction to compare the photo against that step’s goal, and the person’s progress photos:

```swift
var imagePrompts: [Prompt] = []
for photo in photos {
    imagePrompts.append(try await photo.toPrompt())
}
let prompt = Prompt {
    "I'm working on step \(stepNumber) of the tutorial."
    if let stepContent {
        "Step \(stepNumber): \(stepContent)"
    }
    """
    Here is my progress photo. First describe what you see and compare \
    it to the goal of step \(stepNumber). Then provide feedback sections. \
    Finally, set isCurrentStepComplete to true only if the photo clearly \
    shows step \(stepNumber) is complete.
    """
    imagePrompts
}
let stream = session.streamResponse(
    to: prompt,
    generating: CoachFeedback.self
)
try await coach.processStream(stream)
```

The response type, `CoachFeedback`, carries a Boolean the app reads to drive its UI flow. The `@Guide` on `isCurrentStepComplete` spells out exactly when to set it:

```swift
@Generable
struct CoachFeedback: Codable {
    @Guide(description: "Break feedback into 2-3 sections with titles like 'What You Did Well', 'Try This Instead', or 'Next Steps'.")
    var sections: [CoachSection]
    @Guide(description: "True ONLY if the photo clearly and unambiguously demonstrates that the user has completed the specific goal of the current step. Set to false if the photo shows a mistake, an unrelated subject, insufficient progress, or if you are uncertain. Err strongly on the side of false.")
    var isCurrentStepComplete: Bool
    @Guide(description: "A short (1-2 sentence) encouraging message shown when isCurrentStepComplete is true. Leave blank if isCurrentStepComplete is false.")
    var completionMessage: String?
}
```

A Boolean field with a strict guide acts as a small classifier: the app advances the tutorial only when the model is confident the step is done. Coach reuses the tutorial-mode profile because judging a progress photo against a step’s goal is harder than recognizing a finished piece. When the `serverModel` is PCC, that profile activates `.reasoningLevel(.deep)`; on device, Coach uses the simpler tutorial fallback. The prompt-and-decode API stays the same in either case.

The `isCurrentStepComplete` field only gates step advancement; the model still produces feedback sections when the photo doesn’t match, so the person sees what went wrong even when Coach holds the tutorial in place.

Because the photos come from people, the sample designs for refusals and guardrail violations so the app responds gracefully when the model declines. For more information, see [`Improving the safety of generative model output`](improving-the-safety-of-generative-model-output.md).

#### Stream Partial Results

The same [`LanguageModelSession.ResponseStream`](languagemodelsession/responsestream.md) API supports different presentation patterns. Brainstorm shows ideas progressively as they finalize. Its `processStream` walks the [`PartiallyGenerated`](generable/partiallygenerated.md) value and advances an index, filling in each idea as more text streams in:

```swift
func processStream(
    _ stream: LanguageModelSession.ResponseStream<BrainstormIdeaList>
) async throws {
    for try await partialResponse in stream where partialResponse.content.ideas != nil {
        for (offset, partialIdea) in partialResponse.content.ideas!.enumerated() {
            let title = partialIdea.title ?? ""
            let desc = partialIdea.description ?? ""
            if newIdeas.count <= offset {
                newIdeas.append(BrainstormIdea(title: title, description: desc))
            } else {
                newIdeas[offset].title = title
                newIdeas[offset].description = desc
            }
        }
    }
    ideas.append(contentsOf: newIdeas)
    newIdeas = []
}
```

A different approach is to buffer the stream and publish only the final value. That’s what you want when the response is prose that reads oddly if it rewrites itself midsentence:

```swift
func processStream(_ stream: LanguageModelSession.ResponseStream<CoachFeedback>) async throws {
    state = .loading
    // Buffer the full response and only publish when streaming completes.
    var finalContent: CoachFeedback.PartiallyGenerated?
    for try await partial in stream {
        finalContent = partial.content
    }
    if let finalContent {
        state = .responded(finalContent)
    }
}
```

Animate responses when partial output reads well, and buffer them when it doesn’t. Streaming consumes context as the response grows, so a long-running session tracks its budget across turns. For more information, see [`Managing the context window`](managing-the-context-window.md).

#### Go Further with Origami

The same building blocks reach beyond Brainstorm and Coach. A separate, on-device session backed by [`SystemLanguageModel`](systemlanguagemodel.md) powers a tap-to-explain terminology feature. After the app generates a tutorial, it makes a one-shot `respond(to:generating:)` call to pull out the terms worth explaining along the way. Origami uses the same prompt-and-decode API described earlier, just on a smaller model.

```swift
let response = try await session.respond(
    to: tutorialBody,
    generating: ExtractedTerms.self
)
```

Origami also draws on other parts of the Foundation Models framework, like tool calling and key-value caching. To learn more, see [`Expanding generation with tool calling`](expanding-generation-with-tool-calling.md) and [`Optimizing key-value caching in language model sessions`](optimizing-key-value-caching-in-language-model-sessions.md).

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/origami-crafting-a-dynamic-tutorial-for-apple-intelligence)*