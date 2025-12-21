# near

**Framework**: RealityKit  
**Kind**: property

The minimum distance in meters from the camera that the camera can see.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var near: Float
```

#### Discussion

The value defaults to `1.0` centimeter. Use a value greater than `0.0` and less than the value of [`far`](orthographiccameracomponent/far.md). The renderer clips any surface closer than the `near` point.

## See Also

- [var far: Float](orthographiccameracomponent/far.md)
  The maximum distance in meters from the camera that the camera can see.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orthographiccameracomponent/near)*