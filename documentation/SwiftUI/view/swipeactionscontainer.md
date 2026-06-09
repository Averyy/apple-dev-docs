# swipeActionsContainer()

**Framework**: SwiftUI  
**Kind**: method

Coordinates swipe action dismissal and mutual exclusion across rows in a container.

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
func swipeActionsContainer() -> some View
```

#### Discussion

Apply this modifier to a `ScrollView` or other container that holds rows using the [`swipeActions(edge:allowsFullSwipe:content:)`](view/swipeactions(edge:allowsfullswipe:content:).md) modifier. The container ensures that:

- Only one row’s swipe actions are revealed at a time.
- Scrolling the container dismisses any open actions.
- Tapping outside the active row dismisses its actions.

`List` provides this coordination automatically. Use `swipeActionsContainer()` when building custom row-based layouts that use `ScrollView`, `LazyVStack`, or similar containers.

```swift
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item)
                .swipeActions {
                    Button("Delete", role: .destructive) {
                        delete(item)
                    }
                }
        }
    }
}
.swipeActionsContainer()
```

Applying this modifier to a `List` is a no-op, since `List` already provides this coordination.

## See Also

- [func swipeActions(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> some View, onPresentationChanged: (Bool) -> Void) -> some View](view/swipeactions(edge:allowsfullswipe:content:onpresentationchanged:).md)
  Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/swipeactionscontainer())*