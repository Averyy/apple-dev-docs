# searchable(text:isPresented:placement:prompt:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Marks this view as searchable with programmatic presentation of the search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource) -> some View
```

```swift
nonisolated
func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey) -> some View
```

```swift
nonisolated
func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: S) -> some View where S : StringProtocol
```

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md). For information about presenting a search field programmatically, see [Managing search interface activation](../managing-search-interface-activation.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `isPresented`: A [`Binding`](../binding.md) that controls the presented state of search.
- `placement`: The preferred placement of the search field within the containing view hierarchy.
- `prompt`: A [`Text`](../text.md) view representing the prompt of the search field which provides users with guidance on what to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:ispresented:placement:prompt:)-5hhxx)*