# onDrag(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Activates this view as the source of a drag and drop operation.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
```

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [`contentShape(_:_:eoFill:)`](./contentshape%28_,_,eofill%29.md) with a [`dragPreview`](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

If you want to show a different preview, you can use [`onDrag(_:preview:)`](./ondrag%28_,preview%29.md).

To use `Transferable` types directly and access a richer feature set — including multi-item drag via [`dragContainer(for:in:_:)`](./dragcontainer%28for,in,_%29.md) — use [`draggable(_:)`](./draggable%28_%29.md) instead.

> ❗ **Important**: Don’t dispatch work to the main actor while exporting the item. Doing so isn’t supported and might cause a hang. If you register data representations on the item provider yourself, make sure their completion handlers don’t dispatch to the main thread.

## Parameters

- `data`: A closure that returns a single [`NSItemProvider`](../../Foundation/nsitemprovider.md) that represents the draggable data from this view.

## See Also

### Moving items using item providers
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](./itemprovider%28_%29.md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](./ondrag%28_,preview%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ondrag(_:))*