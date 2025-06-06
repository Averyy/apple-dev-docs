# extent

**Framework**: ARKit  
**Kind**: property

The extent of the detected barcode’s bounds.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var extent: SIMD3<Float> { get }
```

#### Discussion

The width of the detected barcode is the length along the X-axis, prior to rotation about the Y-axis.

The height of the detected barcode is the length along the Z-axis, prior to rotation about the Y-axis.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor/extent)*