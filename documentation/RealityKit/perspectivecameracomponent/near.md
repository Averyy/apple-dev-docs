# near

**Framework**: RealityKit  
**Kind**: property

The minimum distance in meters from the camera that the camera can see.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var near: Float
```

#### Discussion

The value defaults to `1.0` centimeter. Use a value greater than `0.0` and less than the value of [`far`](perspectivecameracomponent/far.md). The renderer clips any surface closer than the `near` point.

## See Also

- [var far: Float](perspectivecameracomponent/far.md)
  The maximum distance in meters from the camera that the camera can see.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perspectivecameracomponent/near)*