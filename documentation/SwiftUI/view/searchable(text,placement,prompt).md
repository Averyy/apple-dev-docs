# searchable(text:placement:prompt:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource) -> some View
```

**Other overloads**:

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey) -> some View
```

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View
```

```swift
nonisolated
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: S) -> some View where S : StringProtocol
```

## Mentions

- [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md)
- [Managing search interface activation](../managing-search-interface-activation.md)
- [Suggesting search terms](../suggesting-search-terms.md)

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: The preferred placement of the search field within the containing view hierarchy.
- `prompt`: Text resource for the localized prompt of the search field which provides users with guidance on what to search for.

## See Also

### Searching your app’s data model
- [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md)
  Present an interface that people can use to search for content in your app.
- [Performing a search operation](../performing-a-search-operation.md)
  Update search results based on search text and optional tokens that you store.
- [func searchable(text:tokens:placement:prompt:token:)](./searchable%28text,tokens,placement,prompt,token%29.md)
  Marks this view as searchable with text and tokens.
- [func searchable(text:editableTokens:placement:prompt:token:)](./searchable%28text,editabletokens,placement,prompt,token%29.md)
  Marks this view as searchable, which configures the display of a search field.
- [struct SearchFieldPlacement](../searchfieldplacement.md)
  The placement of a search field in a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:))*