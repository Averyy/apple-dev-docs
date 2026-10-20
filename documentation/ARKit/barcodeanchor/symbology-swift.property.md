# symbology

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The symbology of the detected barcode.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var symbology: BarcodeAnchor.Symbology { get }
```

## See Also

### Getting barcode information
- [var extent: SIMD3<Float>](./extent.md)
  The extent of the detected barcode’s bounds.
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the barcode anchor to the origin coordinate system.
- [var payloadData: Data](./payloaddata.md)
  The encoded payload data of the detected barcode.
- [var payloadString: String?](./payloadstring.md)
  The decoded payload string value of the detected barcode.
- [BarcodeAnchor.Symbology](./symbology-swift.enum.md)
  Values that describe specific kinds of barcodes.
- [var id: UUID](./id.md)
  The unique identifier of an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor/symbology-swift.property)*