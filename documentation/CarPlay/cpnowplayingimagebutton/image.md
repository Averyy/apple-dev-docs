# image

**Framework**: CarPlay  
**Kind**: property

The image that the button displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var image: UIImage? { get }
```

#### Discussion

The button displays images no larger than [`CPNowPlayingButtonMaximumImageSize`](cpnowplayingbuttonmaximumimagesize.md). If you use an animated image, this property returns the first image in the animation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingimagebutton/image)*