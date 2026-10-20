# CFURLPathStyle.cfurlhfsPathStyle

**Framework**: Core Foundation  
**Kind**: case  
**Role**: Case

Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Carbon File Manager is deprecated, use kCFURLPOSIXPathStyle where possible

## Declaration

```swift
case cfurlhfsPathStyle
```

```c
kCFURLHFSPathStyle
```

## See Also

### Constants
- [CFURLPathStyle.cfurlposixPathStyle](./cfurlposixpathstyle.md)
  Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.
- [CFURLPathStyle.cfurlWindowsPathStyle](./cfurlwindowspathstyle.md)
  Indicates a Windows style path name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/cfurlhfspathstyle)*