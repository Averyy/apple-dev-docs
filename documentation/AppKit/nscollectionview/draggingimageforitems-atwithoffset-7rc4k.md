# draggingImageForItems(at:with:offset:)

**Framework**: AppKit  
**Kind**: method

Returns an image to use for dragging the specified items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func draggingImageForItems(at indexPaths: Set<IndexPath>, with event: NSEvent, offset dragImageOffset: NSPointPointer) -> NSImage
```

#### Return Value

The image to use for the dragged items.

#### Discussion

The default implementation of this method creates an image using the visible portions of the dragged items. The resulting image is a snapshot of the dragged items as they currently appear in the collection view but rendered with additional transparency to indicate they are part of a drag operation. This method also updates the `dragImageOffset` parameter to an appropriate point for dragging the resulting image.

If the delegate implements the [`collectionView(_:draggingImageForItemsAt:with:offset:)`](nscollectionviewdelegate/collectionview(_:draggingimageforitemsat:with:offset:)-898js.md) method, the collection view method obtains the drag image from that method instead. If the delegate does not implement that method, the collection view uses the image returned by this method.

## Parameters

- `indexPaths`: The set of   objects corresponding to the items being dragged.
- `event`: The mouse-down event that began the drag operation.
- `dragImageOffset`: The offset value to use when positioning the image. On input, the point is  , which centers the returned image under the mouse. Custom implementations can return a different point that repositions the drag image by the specified offset values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/draggingimageforitems(at:with:offset:)-7rc4k)*