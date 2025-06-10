# contentTagging

**Framework**: Foundation Models  
**Kind**: property

A use case for content tagging.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let contentTagging: SystemLanguageModel.UseCase
```

#### Discussion

Content tagging produces a list of categorizing tags based on the input prompt. When specializing the model for the `contentTagging` use case, it always responds with tags. The tagging capabilities of the model include detecting topics, emotions, actions, and objects.

```swift
// Create an instance of the model with the content tagging use case.
let model = SystemLanguageModel(useCase: .contentTagging)

// Initialize a session with the model.
let session = LanguageModelSession(model: model)
```

If you don’t provide [`Instructions`](instructions.md) to the session, the model generates topic-related tags by default. To generate other kinds of tags, like emotions, actions, or objects, specify the kind of tag either in instructions or in a [`Generable`](generable.md) output type.

```swift
let instructions = """
    Tag the three most important actions, emotions, objects, \
    and topics in the given input text
    """
```

The code below prompts the model to respond about a picnic at the beach with tags like “outdoor activity,” “beach,” and “picnic”:

```swift
let prompt = """
    Today we had a lovely picnic with friends at the beach.
    """
let response = try await session.respond(
    to: prompt,
    generating: ContentTaggingResult.self
)
```

Content tagging works best if you define an output structure using guided generation. The code below uses [`Generable`](generable.md) guide descriptions to specify the kinds and quantities of tags the model should produce:

```swift
@Generable
struct ContentTaggingResult {
    @Guide(
        description: "Most important actions in the input text",
        .maximumCount(3)
    )
    let actions: [String]
    @Guide(
        description: "Most important emotions in the input text",
        .maximumCount(3)
    )
    let emotions: [String]
    @Guide(
        description: "Most important objects in the input text",
        .maximumCount(3)
    )
    let objects: [String]
    @Guide(
        description: "Most important topics in the input text",
        .maximumCount(3)
    )
    let topics: [String]
}
```

> **Note**: Content tagging currently only produces tags in English, and can’t be used with tool calling.

## See Also

- [static let general: SystemLanguageModel.UseCase](systemlanguagemodel/usecase/general.md)
  A use case for general prompting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/usecase/contenttagging)*