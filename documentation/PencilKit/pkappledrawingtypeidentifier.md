# PKAppleDrawingTypeIdentifier

**Framework**: PencilKit  
**Kind**: var  
**Role**: Global Variable

The uniform type identifier for data associated with a drawing object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
let PKAppleDrawingTypeIdentifier: CFString
```

```c
extern CFStringRef const PKAppleDrawingTypeIdentifier;
```

#### Discussion

Use this type when reading or writing drawing data. For example, use this type to determine if you can read data from the pasteboard.

## See Also

### Getting the drawing data
- [var strokes: [PKStroke]](./pkdrawing-swift.struct/strokes.md)
  The array of strokes that make up the drawing.
- [func dataRepresentation() -> Data](./pkdrawing-swift.struct/datarepresentation%28%29.md)
  Returns a raw data representation of the rendered content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkappledrawingtypeidentifier)*