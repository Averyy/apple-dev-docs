# readRTFD(fromFile:)

**Framework**: AppKit  
**Kind**: method

Attempts to read the RTFD file at the specified path.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func readRTFD(fromFile path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

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