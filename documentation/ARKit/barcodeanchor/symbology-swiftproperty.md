# symbology

**Framework**: ARKit  
**Kind**: property

The symbology of the detected barcode.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var symbology: BarcodeAnchor.Symbology { get }
```

## See Also

- [var extent: SIMD3<Float>](barcodeanchor/extent.md)
  The extent of the detected barcode’s bounds.
- [var originFromAnchorTransform: simd_float4x4](barcodeanchor/originfromanchortransform.md)
  The transform from the barcode anchor to the origin coordinate system.
- [var payloadData: Data](barcodeanchor/payloaddata.md)
  The encoded payload data of the detected barcode.
- [var payloadString: String?](barcodeanchor/payloadstring.md)
  The decoded payload string value of the detected barcode.
- [BarcodeAnchor.Symbology](barcodeanchor/symbology-swift.enum.md)
  Values that describe specific kinds of barcodes.
- [var id: UUID](barcodeanchor/id.md)
  The unique identifier of an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor/symbology-swift.property)*