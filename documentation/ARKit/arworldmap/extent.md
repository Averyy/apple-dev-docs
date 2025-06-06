# extent

**Framework**: ARKit  
**Kind**: property

The size of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var extent: simd_float3 { get }
```

#### Discussion

The [`extent`](arworldmap/extent.md) and [`center`](arworldmap/center.md) properties together define a bounding box for the data recorded in the world map.

## See Also

- [var anchors: [ARAnchor]](arworldmap/anchors.md)
  The set of anchors recorded in the world map.
- [var center: simd_float3](arworldmap/center.md)
  The center point of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldmap/extent)*