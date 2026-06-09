# leftPolygonPoints

**Framework**: ARKit  
**Kind**: property

Left eye polygon boundary points defining the preset field of view.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var leftPolygonPoints: [simd_float4] { get }
```

#### Discussion

Each point represents a vertex of the polygon boundary, ordered to form a continuous polygon. Points are expressed in the anchor’s coordinate frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/fieldofviewanchor/leftpolygonpoints)*