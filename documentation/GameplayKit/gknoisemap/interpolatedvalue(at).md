# interpolatedValue(at:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns the value at the specified position in the noise map, interpolating results for positions not on the discrete sample grid.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func interpolatedValue(at position: vector_float2) -> Float
```

```objc
- (float) interpolatedValueAtPosition:(vector_float2) position;
```

## Return Value

The value at the specified position.

## Discussion

When you create a noise map from a [`GKNoise`](../gknoise.md) object, GameplayKit performs the noise generation and processing computations necessary to fill a discrete grid with noise samples. (You specify the size of the grid and its number of samples in the [`init(_:size:origin:sampleCount:seamless:)`](./init%28_,size,origin,samplecount,seamless%29.md) initializer.) You can use this method to get noise values for arbitrary positions in the noise field, regardless of whether those positions are aligned with the discrete grid. When you query a position not aligned with the grid, this method automatically samples nearby grid positions and interpolates the results.

To query only positions within the discrete sample grid, use the [`value(at:)`](./value%28at%29.md) method instead.

## Parameters

- `position`: The position to query in the noise map. Must be within the rectangle defined by the noise map’s [`origin`](./origin.md) and [`size`](./size.md) properties.

## See Also

### Accessing Noise Values
- [func value(at: vector_int2) -> Float](./value%28at%29.md)
  Returns the value at the specified position in the noise map’s discrete sample grid.
- [func setValue(Float, at: vector_int2)](./setvalue%28_,at%29.md)
  Sets the value at the specified position in the noise map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoisemap/interpolatedvalue(at:))*