# stringValue

**Framework**: AVFoundation  
**Kind**: property

Returns the error-corrected data decoded into a human-readable string.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 9.0+

## Declaration

```swift
var stringValue: String? { get }
```

#### Discussion

The value of this property is an `NSString` created by decoding the binary payload according to the format of the machine-readable code, or `nil` if a string representation cannot be created.

## See Also

- [var corners: [CGPoint]](avmetadatamachinereadablecodeobject/corners-58qbe.md)
  A Swift array of corner points.
- [var descriptor: CIBarcodeDescriptor?](avmetadatamachinereadablecodeobject/descriptor.md)
  A barcode description for use in Core Image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/stringvalue)*