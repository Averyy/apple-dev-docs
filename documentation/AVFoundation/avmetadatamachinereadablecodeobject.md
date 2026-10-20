# AVMetadataMachineReadableCodeObject

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Barcode information detected by a metadata capture output.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 9.0+

## Declaration

```swift
class AVMetadataMachineReadableCodeObject
```

```objc
@interface AVMetadataMachineReadableCodeObject : AVMetadataObject
```

#### Overview

The `AVMetadataMachineReadableCodeObject` class is a concrete subclass of [`AVMetadataObject`](./avmetadataobject.md) defining the features of a detected one-dimensional or two-dimensional barcode.

An `AVMetadataMachineReadableCodeObject` instance represents a single detected machine readable code in an image.  It’s an immutable object describing the features and payload of a barcode.

On supported platforms, the [`AVCaptureMetadataOutput`](./avcapturemetadataoutput.md) class outputs arrays of detected machine readable code objects.

## Topics

### Getting machine-readable code values
- [var corners: [CGPoint]](./avmetadatamachinereadablecodeobject/corners-58qbe.md)
  A Swift array of corner points.
- [var descriptor: CIBarcodeDescriptor?](./avmetadatamachinereadablecodeobject/descriptor.md)
  A barcode description for use in Core Image.
- [var stringValue: String?](./avmetadatamachinereadablecodeobject/stringvalue.md)
  Returns the error-corrected data decoded into a human-readable string.
### Constants
- [Machine-readable object types](./machine-readable-object-types.md)
  Constants used to specify the type of barcode to scan.

## Relationships

### Inherits From
- [AVMetadataObject](./avmetadataobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject)*