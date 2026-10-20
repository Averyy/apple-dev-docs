# strokes

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

An array of strokes used to represent the drawing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var strokes: [PKStroke] { get }
```

```objc
@property (nonatomic, readonly) NSArray<PKStroke *> * strokes;
```

## See Also

### Getting the drawing data
- [func dataRepresentation() -> Data](./datarepresentation%28%29.md)
  Returns a representation of the rendered content as data.
- [let PKAppleDrawingTypeIdentifier: CFString](../pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/strokes)*