# permanentLink

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A permanent URL (permalink) that your app can use to access the post.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var permanentLink: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * permanentLink;
```

## See Also

### Getting the Shared Items
- [var attachmentFileURLs: [URL]?](./attachmentfileurls.md)
  An array of NSURL objects representing the files that were shared.
- [var messageBody: String?](./messagebody.md)
  The message body as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/permanentlink)*