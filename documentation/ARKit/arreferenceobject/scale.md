# scale

**Framework**: ARKit  
**Kind**: property

A scale factor for the local coordinate space the reference object defines.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var scale: simd_float3 { get }
```

#### Discussion

Multiplying the [`extent`](arreferenceobject/extent.md) by this scale results in the physical size of the object in meters.

## See Also

- [var name: String?](arreferenceobject/name.md)
  A descriptive name for the reference object.
- [var resourceGroupName: String?](arreferenceobject/resourcegroupname.md)
- [var center: simd_float3](arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](arreferenceobject/extent.md)
  The size of the reference object’s space-mapping data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/scale)*