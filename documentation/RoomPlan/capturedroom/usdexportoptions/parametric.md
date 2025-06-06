# parametric

**Framework**: RoomPlan  
**Kind**: property

An export option that formats the output file as a collection of size-dependent primitives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static let parametric: CapturedRoom.USDExportOptions
```

#### Discussion

A parametric model stores elements as unit-sized cubes versus polygonal units. The scale of each element determines whether it appears as a plane or a box.

## See Also

- [static let mesh: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/mesh.md)
  An export option that formats the output file as a collection of size-independant triangles that connect to form a mesh.
- [static let model: CapturedRoom.USDExportOptions](capturedroom/usdexportoptions/model.md)
  An export option that formats the output file as a collection of 3D models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions/parametric)*