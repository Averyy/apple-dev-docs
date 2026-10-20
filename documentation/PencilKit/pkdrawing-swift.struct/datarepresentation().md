# dataRepresentation()

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns a raw data representation of the rendered content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func dataRepresentation() -> Data
```

#### Return Value

A new [`NSData`](../../Foundation/nsdata.md) object that contains the entire contents of the drawing.

## See Also

### Getting the drawing data
- [var strokes: [PKStroke]](./strokes.md)
  The array of strokes that make up the drawing.
- [let PKAppleDrawingTypeIdentifier: CFString](../pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/datarepresentation())*