# attachmentFileURLs

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of NSURL objects representing the files that were shared.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var attachmentFileURLs: [URL]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSURL *> * attachmentFileURLs;
```

## See Also

### Getting the Shared Items
- [var messageBody: String?](./messagebody.md)
  The message body as a string.
- [var permanentLink: URL?](./permanentlink.md)
  A permanent URL (permalink) that your app can use to access the post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/attachmentfileurls)*