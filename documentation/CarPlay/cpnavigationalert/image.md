# image

**Framework**: CarPlay  
**Kind**: property

An image displayed in the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var image: UIImage? { get }
```

#### Discussion

The navigation alert doesn’t support animated images. If `image` references an animated image, the alert displays first image in the animation sequence.

## See Also

- [var imageSet: CPImageSet?](cpnavigationalert/imageset.md)
  An image set displayed in the navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/image)*