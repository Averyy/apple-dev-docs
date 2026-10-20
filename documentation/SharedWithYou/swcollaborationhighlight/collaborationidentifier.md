# collaborationIdentifier

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

A unique identifier that the app hosting the collaboration provides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var collaborationIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * collaborationIdentifier;
```

#### Discussion

This identifier is unique across platforms and sharing sessions.

## See Also

### Accessing collaboration attributes
- [var contentType: UTType](./contenttype.md)
  The UTI type for this collaboration highlight.
- [var creationDate: Date](./creationdate.md)
  The date the system creates this file.
- [var title: String?](./title.md)
  The title of the collaboration highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationhighlight/collaborationidentifier)*