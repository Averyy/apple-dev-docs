# shadingImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An image that looks like a shaded sphere enclosed in a square.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shadingImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * shadingImage;
```

## See Also

### Instance Properties
- [var center: CGPoint](./center.md)
  The x and y position to use as the center of the effect.
- [var extent: CGRect](./extent.md)
  A rectangle that defines the extent of the effect.
- [var scale: Float](./scale.md)
  A value that determines whether the ripple starts as a bulge (a higher value) or a dimple (a lower value).
- [var width: Float](./width.md)
  The width of the ripple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirippletransition/shadingimage)*