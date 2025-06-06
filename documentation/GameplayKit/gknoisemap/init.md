# init()

**Framework**: GameplayKit  
**Kind**: init

Initializes a noise map with a constant noise value of zero throughout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init()
```

#### Return Value

A new noise map object.

#### Discussion

This convenience initializer is equivalent to creating a [`GKNoise`](gknoise.md) object from [`GKConstantNoiseSource`](gkconstantnoisesource.md) output with a constant value of zero, then using the [`init(_:)`](gknoisemap/init(_:).md) initializer to create a noise map from the result.

## See Also

- [convenience init(GKNoise)](gknoisemap/init(_:).md)
  Initializes a noise map by sampling from the specified noise object.
- [init(GKNoise, size: vector_double2, origin: vector_double2, sampleCount: vector_int2, seamless: Bool)](gknoisemap/init(_:size:origin:samplecount:seamless:).md)
  Creates a noise map by sampling from the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/init())*