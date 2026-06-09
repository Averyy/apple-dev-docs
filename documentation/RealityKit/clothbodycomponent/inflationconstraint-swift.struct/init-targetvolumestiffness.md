# init(targetVolume:stiffness:)

**Framework**: RealityKit  
**Kind**: init

Creates an inflation configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(targetVolume: Float, stiffness: Float = 1.0)
```

## Parameters

- `targetVolume`: The target volume (in ㎥) that the body tries to match.
- `stiffness`: The resistance to diverge from the target volume. Valid range is [0.0, 1.0].

## See Also

- [init(stiffness: Float)](clothbodycomponent/inflationconstraint-swift.struct/init(stiffness:).md)
  Creates an inflation configuration that defaults to the mesh volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct/init(targetvolume:stiffness:))*