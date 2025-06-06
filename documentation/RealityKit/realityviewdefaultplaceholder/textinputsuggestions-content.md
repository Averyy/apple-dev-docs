# textInputSuggestions(_:content:)

**Framework**: RealityKit  
**Kind**: method

Configures the text input suggestions for this view.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func textInputSuggestions<Data, Content>(_ data: Data, @ViewBuilder content: @escaping (Data.Element) -> Content) -> some View where Data : RandomAccessCollection, Content : View, Data.Element : Identifiable
```

#### Discussion

You can suggest text completions during a text input operation by providing data to this modifier. The interface presents the suggestion views as a list of choices when someone activates the text editing interface.

Associate a string with each suggestion view by adding the `View/textInputCompletion(_:)` modifier to the view.

Use `Label` to get platform-standard visual representations of suggestion text accompanied with images, and `Section` for labelled sections of results.

## Parameters

- `data`: The data that is used to create views dynamically.
- `content`: The view builder that creates views dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/textinputsuggestions(_:content:))*