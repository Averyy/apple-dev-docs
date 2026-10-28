# validateContent()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Performs validation of the current content and updates the state of the Post button, if appropriate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
func validateContent()
```

```objc
- (void) validateContent;
```

## Discussion

By default, `validateContent` calls [`isContentValid()`](./iscontentvalid%28%29.md), performs internal content validation, and updates the state of the Post button, if necessary. You should call this method if you change any data that your implementation of `isContentValid` uses to test for content validity.

## See Also

### Validating Content
- [var charactersRemaining: NSNumber!](./charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func isContentValid() -> Bool](./iscontentvalid%28%29.md)
  A Boolean value that indicates whether the current content and attachments are valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/validatecontent())*