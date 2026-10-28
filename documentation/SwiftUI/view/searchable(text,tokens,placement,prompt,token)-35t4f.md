# searchable(text:tokens:placement:prompt:token:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Marks this view as searchable with text and tokens.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: S, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the search field.
- `placement`: The preferred placement of the search field within the containing view hierarchy.
- `prompt`: A string representing the prompt of the search field which provides users with guidance on what to search for.
- `token`: A content builder that creates a view given an element in tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:)-35t4f)*