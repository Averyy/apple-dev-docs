# descriptor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A barcode description for use in Core Image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 11.0+

## Declaration

```swift
var descriptor: CIBarcodeDescriptor? { get }
```

```objc
@property (readonly, nullable) CIBarcodeDescriptor * descriptor;
```

## See Also

### Getting machine-readable code values
- [var corners: [CGPoint]](./corners-58qbe.md)
  A Swift array of corner points.
- [var stringValue: String?](./stringvalue.md)
  Returns the error-corrected data decoded into a human-readable string.
- [corners](./corners-8f6bv.md)
  The points defining the (x, 	y) locations of the corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/descriptor)*