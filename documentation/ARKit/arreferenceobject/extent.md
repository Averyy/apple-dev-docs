# extent

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The size of the reference object’s space-mapping data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var extent: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 extent;
```

## Discussion

The [`extent`](../arworldmap/extent.md) and [`center`](../arworldmap/center.md) properties together define a bounding box for the data recorded in the reference object in its local coordinate system. You define that coordinate system with the transform parameter when calling `extractReferenceObject(transform:center:extent:)`, and can modify it by creating another reference object with [`applyingTransform(_:)`](./applyingtransform%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/extent)*