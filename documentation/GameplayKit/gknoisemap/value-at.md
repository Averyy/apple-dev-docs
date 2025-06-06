# value(at:)

**Framework**: GameplayKit  
**Kind**: method

Returns the value at the specified position in the noise map’s discrete sample grid.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func value(at position: vector_int2) -> Float
```

#### Return Value

The value at the specified position.

#### Discussion

When you create a noise map from a [`GKNoise`](gknoise.md) object, GameplayKit performs the noise generation and processing computations necessary to fill a discrete grid with noise samples. (You specify the size of the grid and its number of samples in the [`init(_:size:origin:sampleCount:seamless:)`](gknoisemap/init(_:size:origin:samplecount:seamless:).md) initializer.) Use this method to get sample values from that grid.

You can also use the [`interpolatedValue(at:)`](gknoisemap/interpolatedvalue(at:).md) method to query positions that are not on the discrete integer grid of samples.

## Parameters

- `position`: The position to query in the noise map’s grid of sampled noise values. Must be within the rectangle from   to the noise map’s   value.

## See Also

- [func interpolatedValue(at: vector_float2) -> Float](gknoisemap/interpolatedvalue(at:).md)
  Returns the value at the specified position in the noise map, interpolating results for positions not on the discrete sample grid.
- [func setValue(Float, at: vector_int2)](gknoisemap/setvalue(_:at:).md)
  Sets the value at the specified position in the noise map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/value(at:))*