# radius

**Framework**: GameplayKit  
**Kind**: property

The radius of the path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var radius: Float { get set }
```

#### Discussion

This property defines the space occupied by the path—think of this space as the area created by sweeping a circle (or sphere, for 3D paths) of the specified along the path from vertex to vertex. Agents with path-related goals will attempt to move to or stay within this area.

## See Also

- [var isCyclical: Bool](gkpath/iscyclical.md)
  A Boolean value that determines whether the path loops around on itself (that is, the path’s end point connects to its start point).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/radius)*