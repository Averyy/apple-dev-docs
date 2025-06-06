# anchors

**Framework**: ARKit  
**Kind**: property

The set of anchors recorded in the world map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var anchors: [ARAnchor] { get set }
```

#### Discussion

This array is a snapshot of [`ARAnchor`](aranchor.md) objects (including subclasses of [`ARAnchor`](aranchor.md)) in the session as of when the world map was captured, including the [`transform`](aranchor/transform.md) for each. When you create a world map, ARKit automatically includes all anchors whose positions are assumed to be static with respect to the environment—that is, anchor classes that don’t conform to [`ARTrackable`](artrackable.md). After you create a world map, you can choose to add more anchors to, or remove anchors from, this list before saving or sharing the map.

When you run a session from a world map (and after ARKit successfully reconciles the map to the user’s current environment), the session automatically includes all anchors from that world map. You can then use those anchors to recreate the placement of virtual content so that it matches the session the world map was captured in.

## See Also

- [var center: simd_float3](arworldmap/center.md)
  The center point of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.
- [var extent: simd_float3](arworldmap/extent.md)
  The size of the world map’s space-mapping data, relative to the world coordinate origin of the session the map was recorded in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldmap/anchors)*