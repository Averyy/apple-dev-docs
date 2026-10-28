# haloOverlap

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The separation of colors in the halo.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var haloOverlap: Float { get set }
```

```objc
@property (nonatomic) float haloOverlap;
```

## Discussion

A value of `0` means the halo colors don’t overlap. A value of `1` means the halo colors fully overlap, creating a white halo.

## See Also

### Instance Properties
- [var center: CGPoint](./center.md)
  The x and y position to use as the center of the halo.
- [var color: CIColor](./color.md)
  The color of the halo.
- [var haloRadius: Float](./haloradius.md)
  The radius of the halo.
- [var haloWidth: Float](./halowidth.md)
  The width of the halo, from its inner radius to its outer radius.
- [var striationContrast: Float](./striationcontrast.md)
  The contrast of the halo colors.
- [var striationStrength: Float](./striationstrength.md)
  The intensity of the halo colors.
- [var time: Float](./time.md)
  The current time of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator/halooverlap)*