# dataRepresentation()

**Framework**: PencilKit  
**Kind**: method

Returns a representation of the rendered content as data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func dataRepresentation() -> Data
```

#### Return Value

A new [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that contains the entire contents of the drawing.

## See Also

- [var strokes: [PKStroke]](pkdrawingreference/strokes.md)
  An array of strokes used to represent the drawing.
- [let PKAppleDrawingTypeIdentifier: CFString](pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/datarepresentation())*