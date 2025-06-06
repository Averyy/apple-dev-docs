# setInitialText(_:)

**Framework**: Social  
**Kind**: method

Sets the initial text to be posted.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setInitialText(_ text: String!) -> Bool
```

#### Return Value

Returns a Boolean value that indicates whether the text was successfully set.

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/swift/false) if `text` does not fit in the currently available character space or if the view controller has already been presented to the user (and therefore cannot be changed). Character limits are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## Parameters

- `text`: The text to add to the post.

## See Also

- [func add(UIImage!) -> Bool](slcomposeviewcontroller/add(_:)-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](slcomposeviewcontroller/add(_:)-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](slcomposeviewcontroller/removeallimages.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](slcomposeviewcontroller/removeallurls.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/setinitialtext(_:))*