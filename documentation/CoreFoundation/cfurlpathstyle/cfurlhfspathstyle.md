# CFURLPathStyle.cfurlhfsPathStyle

**Framework**: Core Foundation  
**Kind**: case

Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case cfurlhfsPathStyle
```

## See Also

- [CFURLPathStyle.cfurlposixPathStyle](cfurlpathstyle/cfurlposixpathstyle.md)
  Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.
- [CFURLPathStyle.cfurlWindowsPathStyle](cfurlpathstyle/cfurlwindowspathstyle.md)
  Indicates a Windows style path name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/cfurlhfspathstyle)*