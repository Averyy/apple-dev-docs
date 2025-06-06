# init(image:)

**Framework**: UIKit  
**Kind**: init

Returns an image view initialized with the specified image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(image: UIImage?)
```

#### Return Value

An initialized image view object.

#### Discussion

The image you specified is used to configure the initial size of the image view itself. Use constraints and the image view’s content mode to adjust the image view’s final size onscreen. This method disables user interactions for the image view by setting the [`isUserInteractionEnabled`](uiimageview/isuserinteractionenabled.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

If you specify an animated image whose duration is greater than `0`, the image view automatically starts playing the animation.

## Parameters

- `image`: The initial image to display in the image view. You may specify an image object that contains an animated sequence of images.

## See Also

- [init(image: UIImage?, highlightedImage: UIImage?)](uiimageview/init(image:highlightedimage:).md)
  Returns an image view initialized with the specified regular and highlighted images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/init(image:))*