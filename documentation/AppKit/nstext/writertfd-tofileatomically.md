# writeRTFD(toFile:atomically:)

**Framework**: AppKit  
**Kind**: method

Writes the receiver’s text as RTF with attachments to a file or directory at `path`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func writeRTFD(toFile path: String, atomically flag: Bool) -> Bool
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/swift/true) on success and [`false`](https://developer.apple.com/documentation/swift/false) on failure. If `atomicFlag` is [`true`](https://developer.apple.com/documentation/swift/true), attempts to write the file safely so that an existing file at `path` is not overwritten, nor does a new file at `path` actually get created, unless the write is successful.

## See Also

- [func readRTFD(fromFile: String) -> Bool](nstext/readrtfd(fromfile:).md)
  Attempts to read the RTFD file at `path`, returning [`true`](https://developer.apple.com/documentation/swift/true) if successful and [`false`](https://developer.apple.com/documentation/swift/false) if not.
- [func rtfd(from: NSRange) -> Data?](nstext/rtfd(from:).md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.
- [func rtf(from: NSRange) -> Data?](nstext/rtf(from:).md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/writertfd(tofile:atomically:))*