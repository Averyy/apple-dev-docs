# CFURLPathStyle

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

Options you can use to determine how CFURL functions parse a file system path name.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CFURLPathStyle
```

```c
enum CFURLPathStyle : CFIndex;
```

## Topics

### Constants
- [CFURLPathStyle.cfurlposixPathStyle](./cfurlpathstyle/cfurlposixpathstyle.md)
  Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.
- [CFURLPathStyle.cfurlhfsPathStyle](./cfurlpathstyle/cfurlhfspathstyle.md)
  Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume.
- [CFURLPathStyle.cfurlWindowsPathStyle](./cfurlpathstyle/cfurlwindowspathstyle.md)
  Indicates a Windows style path name.
### Initializers
- [init?(rawValue: CFIndex)](./cfurlpathstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Miscellaneous
- [enum CFURLComponentType](./cfurlcomponenttype.md)
  The types of components in a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle)*