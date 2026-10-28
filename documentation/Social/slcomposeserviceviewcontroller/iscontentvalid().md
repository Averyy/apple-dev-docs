# isContentValid()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether the current content and attachments are valid.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
func isContentValid() -> Bool
```

```objc
- (BOOL) isContentValid;
```

## Return Value

[`true`](../../Swift/true.md) if the current content and attachments are valid for posting, otherwise [`false`](../../Swift/false.md). The default return value is [`true`](../../Swift/true.md).

## Discussion

This method is automatically called after each change a user makes to the text in the compose view. You can use this method to determine whether the Post button should be enabled and to update [`charactersRemaining`](./charactersremaining.md), if necessary.

A subclass should implement this method to perform custom validation of the user’s content before initiating a post.

## See Also

### Validating Content
- [var charactersRemaining: NSNumber!](./charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func validateContent()](./validatecontent%28%29.md)
  Performs validation of the current content and updates the state of the Post button, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/iscontentvalid())*