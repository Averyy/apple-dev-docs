# far

**Framework**: RealityKit  
**Kind**: property

The maximum distance in meters from the camera that the camera can see.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var far: Float
```

#### Discussion

The value defaults to `1000.0`. Use a value greater than the value of [`near`](orthographiccameracomponent/near.md). The renderer clips any surface beyond the `far` point.

## See Also

- [var near: Float](orthographiccameracomponent/near.md)
  The minimum distance in meters from the camera that the camera can see.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orthographiccameracomponent/far)*