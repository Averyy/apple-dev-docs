# id

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of an anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var id: UUID { get }
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
- [var symbology: BarcodeAnchor.Symbology](./symbology-swift.property.md)
  The symbology of the detected barcode.
- [BarcodeAnchor.Symbology](./symbology-swift.enum.md)
  Values that describe specific kinds of barcodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor/id)*