# removeAllImages()

**Framework**: Social  
**Kind**: method

Removes all images from the post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func removeAllImages() -> Bool
```

#### Return Value

Returns a Boolean value that indicates whether the images were successfully removed.

#### Discussion

If the view controller has already been presented to the user when [`removeAllImages()`](slcomposeviewcontroller/removeallimages().md) is called, the method returns [`false`](https://developer.apple.com/documentation/Swift/false) and the images are not removed.

## See Also

- [func setInitialText(String!) -> Bool](slcomposeviewcontroller/setinitialtext(_:).md)
  Sets the initial text to be posted.
- [func add(UIImage!) -> Bool](slcomposeviewcontroller/add(_:)-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](slcomposeviewcontroller/add(_:)-3mn1w.md)
  Adds a URL to the post.
- [func removeAllURLs() -> Bool](slcomposeviewcontroller/removeallurls.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/removeallimages())*