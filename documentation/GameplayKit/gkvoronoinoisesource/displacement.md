# displacement

**Framework**: GameplayKit  
**Kind**: property

The range of random values to assign to each cell in generated noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var displacement: Double { get set }
```

#### Discussion

A Voronoi noise source generates a field of noise values by randomly picking seed points at random positions in a space, then dividing the space into cells so that all the points in a cell are closer to that cell’s seed point than to any other seed point.

After dividing space into cells, the noise source randomly assigns a unique value to each; the range of values is from negative to positive the value of this property. For example, if the [`displacement`](gkvoronoinoisesource/displacement.md) value is `1.0` (the default), cell values range from `-1.0` to `1.0`.

## See Also

- [var frequency: Double](gkvoronoinoisesource/frequency.md)
  A value that determines the number and size of cells in generated noise.
- [var isDistanceEnabled: Bool](gkvoronoinoisesource/isdistanceenabled.md)
  A Boolean value that specifies whether generated noise values incorporate the distance from each point to the nearest seed point.
- [var seed: Int32](gkvoronoinoisesource/seed.md)
  The value that determines the specific configuration of noise produced by the noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/displacement)*