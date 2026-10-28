# setInitialText(_:)

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Sets the initial text to be posted.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func setInitialText(_ text: String!) -> Bool
```

```objc
- (BOOL) setInitialText:(NSString *) text;
```

## Return Value

Returns a Boolean value that indicates whether the text was successfully set.

## Discussion

This method returns [`false`](../../Swift/false.md) if `text` does not fit in the currently available character space or if the view controller has already been presented to the user (and therefore cannot be changed). Character limits are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](../slrequest.md).

## Parameters

- `text`: The text to add to the post.

## See Also

### Specifying the Contents of the Post
- [func add(UIImage!) -> Bool](./add%28_%29-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](./add%28_%29-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](./removeallimages%28%29.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](./removeallurls%28%29.md)
  Removes all URLs from the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/setinitialtext(_:))*