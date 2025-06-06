# far

**Framework**: RealityKit  
**Kind**: property

The maximum distance in meters from the camera that the camera can see.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var far: Float
```

#### Discussion

The value defaults to `infinity`. Use a value greater than the value of [`near`](perspectivecameracomponent/near.md). The renderer clips any surface beyond the `far` point.

## See Also

- [var near: Float](perspectivecameracomponent/near.md)
  The minimum distance in meters from the camera that the camera can see.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecameracomponent/far)*