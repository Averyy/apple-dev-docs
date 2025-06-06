# prepareThumbnail(of:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Creates a thumbnail image at the specified size asynchronously on a background thread.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func byPreparingThumbnail(ofSize size: CGSize) async -> UIImage?
```

#### Discussion

When displaying an image in a [`UIImageView`](uiimageview.md), you can use the view’s [`contentMode`](uiview/contentmode-swift.property.md) property to clip or scale the image automatically. But when the native image size is much larger than the bounds of the view, decoding the full size image creates unnecessary memory overhead. By creating a thumbnail image at a specified size with this method, you avoid the overhead of decoding the image at its full size.

This method asynchronously creates the thumbnail image on a background thread and calls the completion handler on that thread. If your app updates the UI in the completion handler, schedule the UI update on the main thread.

## Parameters

- `size`: The desired size of the thumbnail.
- `completionHandler`: The completion handler takes the following parameters:

## See Also

- [func preparingForDisplay() -> UIImage?](uiimage/preparingfordisplay.md)
  Decodes an image synchronously and provides a new one for display in views and animations.
- [func prepareForDisplay(completionHandler: (UIImage?) -> Void)](uiimage/preparefordisplay(completionhandler:).md)
  Decodes an image asynchronously and provides a new one for display in views and animations.
- [func preparingThumbnail(of: CGSize) -> UIImage?](uiimage/preparingthumbnail(of:).md)
  Returns a new thumbnail image at the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/preparethumbnail(of:completionhandler:))*