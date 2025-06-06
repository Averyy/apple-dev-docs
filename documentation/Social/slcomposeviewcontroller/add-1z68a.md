# add(_:)

**Framework**: Social  
**Kind**: method

Adds an image to the post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func add(_ image: UIImage!) -> Bool
```

#### Return Value

Returns a Boolean value that indicates whether the image was successfully added.

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/swift/false) if `image` does not fit in the currently available space, or if the view controller has already been presented to the user (and therefore cannot be changed). For the accepted `UIImage` formats, see [`Figure 2`](https://developer.apple.com/documentation/uikit/uiimage#1965930). Image size limits are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## Parameters

- `image`: The image to add to the post.

## See Also

- [func setInitialText(String!) -> Bool](slcomposeviewcontroller/setinitialtext(_:).md)
  Sets the initial text to be posted.
- [func add(URL!) -> Bool](slcomposeviewcontroller/add(_:)-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](slcomposeviewcontroller/removeallimages.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](slcomposeviewcontroller/removeallurls.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/add(_:)-1z68a)*