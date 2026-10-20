# init()

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) init;
```

#### Return Value

A new noise map object.

#### Discussion

This convenience initializer is equivalent to creating a [`GKNoise`](../gknoise.md) object from [`GKConstantNoiseSource`](../gkconstantnoisesource.md) output with a constant value of zero, then using the [`init(_:)`](./init%28_%29.md) initializer to create a noise map from the result.

## See Also

### Creating a Noise Map
- [convenience init(GKNoise)](./init%28_%29.md)
  Initializes a noise map by sampling from the specified noise object.
- [init(GKNoise, size: vector_double2, origin: vector_double2, sampleCount: vector_int2, seamless: Bool)](./init%28_,size,origin,samplecount,seamless%29.md)
  Creates a noise map by sampling from the specified noise object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/init())*