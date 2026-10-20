# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The button’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@NSCopying
var image: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * image;
```

#### Discussion

This property returns the custom image you provide at initialization, or a system image when using a concrete subclass like [`CPContactCallButton`](../cpcontactcallbutton.md).

CarPlay doesn’t support animated images. If you provide an animated image, this property returns the first image in the animation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton/image)*