# imageSet

**Framework**: CarPlay  
**Kind**: property

An image set displayed in the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
var imageSet: CPImageSet? { get }
```

#### Discussion

The navigation alert doesn’t support animated images. If [`imageSet`](cpnavigationalert/imageset.md) references an animated image, the alert displays the first image in the animation sequence.

## See Also

- [var image: UIImage?](cpnavigationalert/image.md)
  An image displayed in the navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/imageset)*