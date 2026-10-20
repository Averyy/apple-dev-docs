# extent

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The size of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.

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

#### Discussion

The [`extent`](./extent.md) and [`center`](./center.md) properties together define a bounding box for the data recorded in the world map.

## See Also

### Examining a World Map
- [var anchors: [ARAnchor]](./anchors.md)
  The set of anchors recorded in the world map.
- [var center: simd_float3](./center.md)
  The center point of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldmap/extent)*