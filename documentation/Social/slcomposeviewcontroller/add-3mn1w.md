# add(_:)

**Framework**: Social  
**Kind**: method

Adds a URL to the post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func add(_ url: URL!) -> Bool
```

#### Return Value

Returns a Boolean value that indicates whether the URL was successfully added.

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/swift/false) if `url` does not fit in the currently available character space or if the view controller has already been presented to the user (and therefore cannot be changed). Character limits are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## Parameters

- `url`: The URL to add to the post.

## See Also

- [func setInitialText(String!) -> Bool](slcomposeviewcontroller/setinitialtext(_:).md)
  Sets the initial text to be posted.
- [func add(UIImage!) -> Bool](slcomposeviewcontroller/add(_:)-1z68a.md)
  Adds an image to the post.
- [func removeAllImages() -> Bool](slcomposeviewcontroller/removeallimages.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](slcomposeviewcontroller/removeallurls.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/add(_:)-3mn1w)*