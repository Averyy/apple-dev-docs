# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image displayed in the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
var image: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * image;
```

## Discussion

The navigation alert doesn’t support animated images. If `image` references an animated image, the alert displays first image in the animation sequence.

## See Also

### Getting the alert image
- [var imageSet: CPImageSet?](./imageset.md)
  An image set displayed in the navigation alert.
- [var alertImage: UIImage?](./alertimage.md)
- [var avatarImage: UIImage?](./avatarimage.md)
- [class var maximumAlertImageSize: CGSize](./maximumalertimagesize.md)
  The maximum image size for the alert image that a @c CPNavigationAlert can display.
- [class var maximumAvatarImageSize: CGSize](./maximumavatarimagesize.md)
  The maximum image size for the avatar image that a @c CPNavigationAlert can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/image)*