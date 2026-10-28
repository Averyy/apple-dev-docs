# PhotogrammetrySession.Request.Detail.custom

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

A custom quality for the model, with specifics defined by the photogrammetry session.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
case custom
```

## Discussion

If you select `.custom`, you can define unique detail parameters by configuring the session with a [`PhotogrammetrySession.Configuration.CustomDetailSpecification`](../../configuration-swift.struct/customdetailspecification-swift.struct.md) instance in a [`customDetailSpecification`](../../configuration-swift.struct/customdetailspecification-swift.property.md). The configuration lets you precisely control the model’s detail level, processing efficiency, and output file size by adjusting properties such as [`maximumPolygonCount`](../../configuration-swift.struct/customdetailspecification-swift.struct/maximumpolygoncount.md), [`textureFormat`](../../configuration-swift.struct/customdetailspecification-swift.struct/textureformat-swift.property.md), and more.

> **Note**: [`customDetailSpecification`](../../configuration-swift.struct/customdetailspecification-swift.property.md) will be applied to every [`PhotogrammetrySession.Request`](../../request.md) that specifies a `.custom` detail in this session.  It has no effect on the other levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/detail/custom)*