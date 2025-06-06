# onDelete(perform:)

**Framework**: SwiftUI  
**Kind**: method

Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [`List`](list.md).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onDelete(perform action: Optional<(IndexSet) -> Void>) -> some DynamicViewContent
```

## Mentions

- [Picking container views for your content](picking-container-views-for-your-content.md)

#### Return Value

A view that calls `action` when elements are deleted from the original view.

## Parameters

- `action`: The action that you want SwiftUI to perform when   elements in the view are deleted. SwiftUI passes a set of indices to the   closure that’s relative to the dynamic view’s underlying collection of   data.

## See Also

- [func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent](dynamicviewcontent/oninsert(of:perform:)-418bq.md)
  Sets the insert action for the dynamic view.
- [func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent](dynamicviewcontent/onmove(perform:).md)
  Sets the move action for the dynamic view.
- [func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some DynamicViewContent](dynamicviewcontent/dropdestination(for:action:).md)
  Sets the insert action for the dynamic view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/ondelete(perform:))*