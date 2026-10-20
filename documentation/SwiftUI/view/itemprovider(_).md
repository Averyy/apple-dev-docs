# itemProvider(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Provides a closure that vends the drag representation to be used for a particular data element.

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
func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View
```

## See Also

### Moving items using item providers
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](./ondrag%28_,preview%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](./ondrag%28_%29.md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of:isTargeted:perform:)](./ondrop%28of,istargeted,perform%29.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of:delegate:)](./ondrop%28of,delegate%29.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [protocol DropDelegate](../dropdelegate.md)
  An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [struct DropProposal](../dropproposal.md)
  The behavior of a drop.
- [enum DropOperation](../dropoperation.md)
  Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [struct DropInfo](../dropinfo.md)
  The current state of a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/itemprovider(_:))*