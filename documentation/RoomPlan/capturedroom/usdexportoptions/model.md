# model

**Framework**: RoomPlan  
**Kind**: property

An export option that formats the output file as a collection of 3D models.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static let model: CapturedRoom.USDExportOptions
```

#### Discussion

This export option works in conjunction with the [`CapturedRoomAttribute`](capturedroomattribute.md) and [`CapturedRoom.ModelProvider`](capturedroom/modelprovider.md) APIs to replace objects the framework identifies as of a particular category, or to have particular attributes, with 3D models that you choose in advance.

## See Also

- [static let parametric: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/parametric.md)
  An export option that formats the output file as a collection of size-dependent primitives.
- [static let mesh: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/mesh.md)
  An export option that formats the output file as a collection of size-independant triangles that connect to form a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions/model)*