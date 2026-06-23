# DynamicViewContent

**Framework**: SwiftUI  
**Kind**: protocol

A type of view that generates views from an underlying collection of data.

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
protocol DynamicViewContent<Data> : View
```

## Topics

### Managing the data
- [var data: Self.Data](dynamicviewcontent/data-swift.property.md)
  The collection of underlying data.
- [associatedtype Data : Collection](dynamicviewcontent/data-swift.associatedtype.md)
  The type of the underlying collection of data.
### Responding to updates
- [func onDelete(perform: Optional<(IndexSet) -> Void>) -> some DynamicViewContent](dynamicviewcontent/ondelete(perform:).md)
  Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [`List`](list.md).
- [func onInsert(of:perform:)](dynamicviewcontent/oninsert(of:perform:).md)
  Sets the insert action for the dynamic view.
- [func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent](dynamicviewcontent/onmove(perform:).md)
  Sets the move action for the dynamic view.
- [func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some DynamicViewContent](dynamicviewcontent/dropdestination(for:action:).md)
  Sets the insert action for the dynamic view.
### Reordering
- [func reorderable() -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable.md)
  Enables reordering of views from this content inside the scope of a reorderable container modifier.
- [func reorderable(collectionID: some Hashable & Sendable) -> some DynamicViewContent<Self.Data>
](dynamicviewcontent/reorderable(collectionid:).md)
  Enables reordering views from this content within and between sections in the scope of a reorderable container modifier.
### Deprecated symbols
- [func onInsert(of: [String], perform: (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent](dynamicviewcontent/oninsert(of:perform:)-40hwa.md)
  Sets the insert action for the dynamic view.

## Relationships

### Inherits From
- [View](view.md)
### Conforming Types
- [ForEach](foreach.md)
- [ModifiedContent](modifiedcontent.md)

## See Also

- [struct ForEach](foreach.md)
  A structure that computes views on demand from an underlying collection of identified data.
- [struct ForEachSectionCollection](foreachsectioncollection.md)
  A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [struct ForEachSubviewCollection](foreachsubviewcollection.md)
  A collection which allows a view to be treated as a collection of its subviews in a for each loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent)*