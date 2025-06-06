# onMove(perform:)

**Framework**: SwiftUI  
**Kind**: method

Sets the move action for the dynamic view.

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
func onMove(perform action: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent
```

#### Return Value

A view that calls `action` when elements are moved within the original view.

## Parameters

- `action`: A closure that SwiftUI invokes when elements in the dynamic   view are moved. The closure takes two arguments that represent the   offset relative to the dynamic view’s underlying collection of data.   Pass   to disable the ability to move items.

## See Also

- [func onDelete(perform: Optional<(IndexSet) -> Void>) -> some DynamicViewContent](dynamicviewcontent/ondelete(perform:).md)
  Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [`List`](list.md).
- [func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent](dynamicviewcontent/oninsert(of:perform:)-418bq.md)
  Sets the insert action for the dynamic view.
- [func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some DynamicViewContent](dynamicviewcontent/dropdestination(for:action:).md)
  Sets the insert action for the dynamic view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/onmove(perform:))*