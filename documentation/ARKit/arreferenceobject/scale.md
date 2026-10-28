# scale

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A scale factor for the local coordinate space the reference object defines.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var scale: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 scale;
```

## Discussion

Multiplying the [`extent`](./extent.md) by this scale results in the physical size of the object in meters.

## See Also

### Examining a Reference Object
- [var name: String?](./name.md)
  A descriptive name for the reference object.
- [var resourceGroupName: String?](./resourcegroupname.md)
- [var center: simd_float3](./center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](./extent.md)
  The size of the reference object’s space-mapping data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/scale)*