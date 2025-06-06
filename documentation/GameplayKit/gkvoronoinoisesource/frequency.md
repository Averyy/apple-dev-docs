# frequency

**Framework**: GameplayKit  
**Kind**: property

A value that determines the number and size of cells in generated noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var frequency: Double { get set }
```

#### Discussion

A Voronoi noise source generates a field of noise values by randomly picking seed points at random positions in a space, then dividing the space into cells so that all the points in a cell are closer to that cell’s seed point than to any other seed point.

Increasing frequency increases the number of seed points in any given unit area of a generated noise map, thus also decreasing the size of the cells that surround them. The default value is `1.0`.

## See Also

- [var displacement: Double](gkvoronoinoisesource/displacement.md)
  The range of random values to assign to each cell in generated noise.
- [var isDistanceEnabled: Bool](gkvoronoinoisesource/isdistanceenabled.md)
  A Boolean value that specifies whether generated noise values incorporate the distance from each point to the nearest seed point.
- [var seed: Int32](gkvoronoinoisesource/seed.md)
  The value that determines the specific configuration of noise produced by the noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/frequency)*