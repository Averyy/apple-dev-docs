# acuteAngle

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The primary angle for the repeating parallelogram tile.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var acuteAngle: Float { get set }
```

```objc
@property (nonatomic) float acuteAngle;
```

#### Discussion

Small values create thin diamond tiles, and higher values create fatter parallelogram tiles.

## See Also

### Instance Properties
- [var angle: Float](./angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](./center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var width: Float](./width.md)
  The width of a tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciparallelogramtile/acuteangle)*