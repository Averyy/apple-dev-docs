# isResponding

**Framework**: Foundation Models  
**Kind**: property

A Boolean value that indicates a response is being generated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var isResponding: Bool { get }
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Discussion

> ❗ **Important**: You should not call any of the respond methods while this property is `true`.

Disable buttons and other interactions to prevent users from submitting a second prompt while the model is responding to their first prompt.

```swift
struct ShopView: View {
    @State var session = LanguageModelSession()
    @State var joke = ""

    var body: some View {
        Text(joke)
        Button("Generate joke") {
            Task {
                assert(!session.isResponding, "It should not be possible to tap this button while the model is responding")
                joke = try await session.respond(to: "Tell me a joke").content
            }
        }
        .disabled(session.isResponding) // Prevent concurrent calls to respond
    }
}
```

## See Also

- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/isresponding)*