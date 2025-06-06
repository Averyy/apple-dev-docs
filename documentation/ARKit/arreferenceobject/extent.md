# extent

**Framework**: ARKit  
**Kind**: property

The size of the reference object’s space-mapping data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var extent: simd_float3 { get }
```

#### Discussion

The [`extent`](arworldmap/extent.md) and [`center`](arworldmap/center.md) properties together define a bounding box for the data recorded in the reference object in its local coordinate system. You define that coordinate system with the transform parameter when calling `extractReferenceObject(transform:center:extent:)`, and can modify it by creating another reference object with [`applyingTransform(_:)`](arreferenceobject/applyingtransform(_:).md).

## See Also

- [var name: String?](arreferenceobject/name.md)
  A descriptive name for the reference object.
- [var resourceGroupName: String?](arreferenceobject/resourcegroupname.md)
- [var center: simd_float3](arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var scale: simd_float3](arreferenceobject/scale.md)
  A scale factor for the local coordinate space the reference object defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/extent)*