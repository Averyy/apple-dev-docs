# removeAllImages()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Removes all images from the post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func removeAllImages() -> Bool
```

```objc
- (BOOL) removeAllImages;
```

#### Return Value

Returns a Boolean value that indicates whether the images were successfully removed.

#### Discussion

If the view controller has already been presented to the user when [`removeAllImages()`](./removeallimages%28%29.md) is called, the method returns [`false`](../../Swift/false.md) and the images are not removed.

## See Also

### Specifying the Contents of the Post
- [func setInitialText(String!) -> Bool](./setinitialtext%28_%29.md)
  Sets the initial text to be posted.
- [func add(UIImage!) -> Bool](./add%28_%29-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](./add%28_%29-3mn1w.md)
  Adds a URL to the post.
- [func removeAllURLs() -> Bool](./removeallurls%28%29.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/removeallimages())*