# Rotation3D.SlerpPath.automatic

**Framework**: Spatial  
**Kind**: case

Spherical linear interpolation along the automatically selected arc between two rotations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
case automatic
```

#### Discussion

For angular separations that are less than or equal to 180°, the spherical linear interpolation along the shortest arc between two rotations, otherwise along the longest arc.

## See Also

- [Rotation3D.SlerpPath.shortest](rotation3d/slerppath/shortest.md)
  Spherical linear interpolation along the shortest arc between two rotations.
- [Rotation3D.SlerpPath.longest](rotation3d/slerppath/longest.md)
  Spherical linear interpolation along the longest arc between two rotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/slerppath/automatic)*