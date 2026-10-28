# isDistanceEnabled

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether generated noise values incorporate the distance from each point to the nearest seed point.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isDistanceEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isDistanceEnabled) BOOL distanceEnabled;
```

## Discussion

A Voronoi noise source generates a field of noise values by randomly picking seed points at random positions in a space, then dividing the space into cells so that all the points in a cell are closer to that cell’s seed point than to any other seed point.

After dividing space into cells, the noise source randomly assigns a unique value to each. If this property’s value is [`false`](../../Swift/false.md) (the default), all points within a cell have the same value, creating a crystalline appearance. If this property’s value is [`true`](../../Swift/true.md), the noise source adds to each point’s value the distance from that point to the nearest seed point. With a low value for the [`displacement`](./displacement.md) property, adding distance to noise can create textures like cracked mud; with a high displacement value, adding distance creates textures like bubbling liquid.

## See Also

### Managing Noise Generation Parameters
- [var frequency: Double](./frequency.md)
  A value that determines the number and size of cells in generated noise.
- [var displacement: Double](./displacement.md)
  The range of random values to assign to each cell in generated noise.
- [var seed: Int32](./seed.md)
  The value that determines the specific configuration of noise produced by the noise source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/isdistanceenabled)*