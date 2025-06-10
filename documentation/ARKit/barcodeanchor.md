# BarcodeAnchor

**Framework**: ARKit  
**Kind**: struct

A barcode’s position in a person’s surroundings.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct BarcodeAnchor
```

#### Overview

A `BarcodeAnchor` describes a barcode that ARKit detects in a person’s surroundings. A barcode anchor has exactly one [`BarcodeSymbology`](https://developer.apple.com/documentation/Vision/BarcodeSymbology) that indicates which type of barcode the framework detects. It also includes properties, such as the barcode’s payload data,  which is a decoded string value of that data.

## Topics

### Getting barcode information
- [var extent: SIMD3<Float>](barcodeanchor/extent.md)
  The extent of the detected barcode’s bounds.
- [var originFromAnchorTransform: simd_float4x4](barcodeanchor/originfromanchortransform.md)
  The transform from the barcode anchor to the origin coordinate system.
- [var payloadData: Data](barcodeanchor/payloaddata.md)
  The encoded payload data of the detected barcode.
- [var payloadString: String?](barcodeanchor/payloadstring.md)
  The decoded payload string value of the detected barcode.
- [var symbology: BarcodeAnchor.Symbology](barcodeanchor/symbology-swift.property.md)
  The symbology of the detected barcode.
- [BarcodeAnchor.Symbology](barcodeanchor/symbology-swift.enum.md)
  Values that describe specific kinds of barcodes.
- [var id: UUID](barcodeanchor/id.md)
  The unique identifier of an anchor.
### Instance Properties
- [var description: String](barcodeanchor/description.md)
  A textual representation of this anchor.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class BarcodeDetectionProvider](barcodedetectionprovider.md)
  An object that provides the real-time position of barcodes the framework detects in a person’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor)*