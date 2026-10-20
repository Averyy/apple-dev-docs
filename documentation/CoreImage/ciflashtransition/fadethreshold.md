# fadeThreshold

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The amount of fade between the flash and the target image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var fadeThreshold: Float { get set }
```

```objc
@property (nonatomic) float fadeThreshold;
```

#### Discussion

The higher the value, the more flash time and the less fade time.

## See Also

### Instance Properties
- [var center: CGPoint](./center.md)
  The x and y position to use as the center of the effect.
- [var color: CIColor](./color.md)
  The color of the light rays emanating from the flash.
- [var extent: CGRect](./extent.md)
  The extent of the flash.
- [var maxStriationRadius: Float](./maxstriationradius.md)
  The radius of the light rays emanating from the flash.
- [var striationContrast: Float](./striationcontrast.md)
  The contrast of the light rays emanating from the flash.
- [var striationStrength: Float](./striationstrength.md)
  The strength of the light rays emanating from the flash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciflashtransition/fadethreshold)*