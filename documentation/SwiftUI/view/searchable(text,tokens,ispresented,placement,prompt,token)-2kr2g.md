# searchable(text:tokens:isPresented:placement:prompt:token:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Marks this view as searchable with text and tokens, as well as programmatic presentation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: S, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ContentBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md). For information about presenting a search field programmatically, see [Managing search interface activation](../managing-search-interface-activation.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the search field.
- `isPresented`: A [`Binding`](../binding.md) that controls the presented state of search.
- `placement`: The preferred placement of the search field within the containing view hierarchy.
- `prompt`: A string representing the prompt of the search field which provides users with guidance on what to search for.
- `token`: A content builder that creates a view given an element in tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:ispresented:placement:prompt:token:)-2kr2g)*