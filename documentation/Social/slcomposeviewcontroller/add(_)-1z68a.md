# add(_:)

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Adds an image to the post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func add(_ image: UIImage!) -> Bool
```

```objc
- (BOOL) addImage:(UIImage *) image;
```

## Return Value

Returns a Boolean value that indicates whether the image was successfully added.

## Discussion

This method returns [`false`](../../Swift/false.md) if `image` does not fit in the currently available space, or if the view controller has already been presented to the user (and therefore cannot be changed). For the accepted `UIImage` formats, see [Figure 2](../../UIKit/uiimage.md#1965930). Image size limits are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](../slrequest.md).

## Parameters

- `image`: The image to add to the post.

## See Also

### Specifying the Contents of the Post
- [func setInitialText(String!) -> Bool](./setinitialtext%28_%29.md)
  Sets the initial text to be posted.
- [func add(URL!) -> Bool](./add%28_%29-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](./removeallimages%28%29.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](./removeallurls%28%29.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/add(_:)-1z68a)*