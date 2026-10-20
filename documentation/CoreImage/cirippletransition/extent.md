# extent

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A rectangle that defines the extent of the effect.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var extent: CGRect { get set }
```

```objc
@property (nonatomic) CGRect extent;
```

## See Also

### Instance Properties
- [var center: CGPoint](./center.md)
  The x and y position to use as the center of the effect.
- [var scale: Float](./scale.md)
  A value that determines whether the ripple starts as a bulge (a higher value) or a dimple (a lower value).
- [var shadingImage: CIImage?](./shadingimage.md)
  An image that looks like a shaded sphere enclosed in a square.
- [var width: Float](./width.md)
  The width of the ripple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirippletransition/extent)*