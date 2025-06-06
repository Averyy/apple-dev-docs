# isContentValid()

**Framework**: Social  
**Kind**: method

A Boolean value that indicates whether the current content and attachments are valid.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
func isContentValid() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the current content and attachments are valid for posting, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The default return value is [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

This method is automatically called after each change a user makes to the text in the compose view. You can use this method to determine whether the Post button should be enabled and to update [`charactersRemaining`](slcomposeserviceviewcontroller/charactersremaining.md), if necessary.

A subclass should implement this method to perform custom validation of the user’s content before initiating a post.

## See Also

- [var charactersRemaining: NSNumber!](slcomposeserviceviewcontroller/charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func validateContent()](slcomposeserviceviewcontroller/validatecontent.md)
  Performs validation of the current content and updates the state of the Post button, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/iscontentvalid())*