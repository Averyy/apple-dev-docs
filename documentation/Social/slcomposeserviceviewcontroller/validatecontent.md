# validateContent()

**Framework**: Social  
**Kind**: method

Performs validation of the current content and updates the state of the Post button, if appropriate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
func validateContent()
```

#### Discussion

By default, `validateContent` calls [`isContentValid()`](slcomposeserviceviewcontroller/iscontentvalid().md), performs internal content validation, and updates the state of the Post button, if necessary. You should call this method if you change any data that your implementation of `isContentValid` uses to test for content validity.

## See Also

- [var charactersRemaining: NSNumber!](slcomposeserviceviewcontroller/charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func isContentValid() -> Bool](slcomposeserviceviewcontroller/iscontentvalid.md)
  A Boolean value that indicates whether the current content and attachments are valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/validatecontent())*