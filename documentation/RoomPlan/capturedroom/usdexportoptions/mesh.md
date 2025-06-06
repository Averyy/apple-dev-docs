# mesh

**Framework**: RoomPlan  
**Kind**: property

An export option that formats the output file as a collection of size-independant triangles that connect to form a mesh.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static let mesh: CapturedRoom.USDExportOptions
```

#### Discussion

A mesh model stores elements as polygonal units. You infer element size based on the bounding box around its vertices.

## See Also

- [static let parametric: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/parametric.md)
  An export option that formats the output file as a collection of size-dependent primitives.
- [static let model: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/model.md)
  An export option that formats the output file as a collection of 3D models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions/mesh)*