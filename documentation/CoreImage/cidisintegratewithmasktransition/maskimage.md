# maskImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An image that defines the shape to use when disintegrating from the source to the target image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var maskImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * maskImage;
```

## See Also

### Instance Properties
- [var shadowDensity: Float](./shadowdensity.md)
  The density of the shadow the mask creates.
- [var shadowOffset: CGPoint](./shadowoffset.md)
  The offset of the shadow the mask creates.
- [var shadowRadius: Float](./shadowradius.md)
  The radius of the shadow the mask creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidisintegratewithmasktransition/maskimage)*