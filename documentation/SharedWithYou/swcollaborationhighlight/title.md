# title

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

The title of the collaboration highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

#### Discussion

The app that hosts the collaboration provides this title.

## See Also

### Accessing collaboration attributes
- [var collaborationIdentifier: String](./collaborationidentifier.md)
  A unique identifier that the app hosting the collaboration provides.
- [var contentType: UTType](./contenttype.md)
  The UTI type for this collaboration highlight.
- [var creationDate: Date](./creationdate.md)
  The date the system creates this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationhighlight/title)*