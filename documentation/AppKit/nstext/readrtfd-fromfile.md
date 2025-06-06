# readRTFD(fromFile:)

**Framework**: AppKit  
**Kind**: method

Attempts to read the RTFD file at `path`, returning [`true`](https://developer.apple.com/documentation/swift/true) if successful and [`false`](https://developer.apple.com/documentation/swift/false) if not.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func readRTFD(fromFile path: String) -> Bool
```

#### Discussion

`path` should be the path for an `.rtf` file or an `.rtfd` file wrapper, not for the RTF file within an `.rtfd` file wrapper.

## See Also

- [func writeRTFD(toFile: String, atomically: Bool) -> Bool](nstext/writertfd(tofile:atomically:).md)
  Writes the receiver’s text as RTF with attachments to a file or directory at `path`.
- [func rtfd(from: NSRange) -> Data?](nstext/rtfd(from:).md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.
- [func rtf(from: NSRange) -> Data?](nstext/rtf(from:).md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/readrtfd(fromfile:))*