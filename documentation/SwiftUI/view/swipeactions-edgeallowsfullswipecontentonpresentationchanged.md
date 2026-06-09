# swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)

**Framework**: SwiftUI  
**Kind**: method

Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func swipeActions(edge: HorizontalEdge = .trailing, allowsFullSwipe: Bool = true, @ContentBuilder content: () -> some View, onPresentationChanged: @escaping (Bool) -> Void) -> some View
```

#### Discussion

Use this overload when you need to react to the swipe actions’s visibility — for example, to dim the row or update surrounding chrome while actions are showing.

```swift
@State private var isSwiped = false

MessageRow(message)
    .opacity(isSwiped ? 0.5 : 1.0)
    .swipeActions(edge: .trailing) {
        Button(role: .destructive) {
            store.delete(message)
        } label: {
            Label("Delete", systemImage: "trash")
        }
    } onPresentationChanged: {
        isSwiped = $0
    }
```

The closure is called with `true` when the row’s swipe actions become visible and `false` when they are dismissed.

## Parameters

- `edge`: The edge of the view to associate the swipe actions with. The default is [`HorizontalEdge.trailing`](horizontaledge/trailing.md).
- `allowsFullSwipe`: A Boolean value that indicates whether a full swipe automatically performs the first action. The default is `true`.
- `content`: The content of the swipe actions.
- `onPresentationChanged`: A closure called when the swipe actions are revealed or dismissed.

## See Also

- [func swipeActionsContainer() -> some View](view/swipeactionscontainer.md)
  Coordinates swipe action dismissal and mutual exclusion across rows in a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/swipeactions(edge:allowsfullswipe:content:onpresentationchanged:))*