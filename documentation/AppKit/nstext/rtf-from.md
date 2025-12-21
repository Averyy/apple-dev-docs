# rtf(from:)

**Framework**: AppKit  
**Kind**: method

Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rtf(from range: NSRange) -> Data?
```

#### Discussion

Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the NSData object as the first argument to `NSPasteboard`’s [`setData(_:forType:)`](nspasteboard/setdata(_:fortype:).md) method, with a second argument of `NSRTFPboardType`.

## See Also

- [func readRTFD(fromFile: String) -> Bool](nstext/readrtfd(fromfile:).md)
  Attempts to read the RTFD file at the specified path.
- [func writeRTFD(toFile: String, atomically: Bool) -> Bool](nstext/writertfd(tofile:atomically:).md)
  Writes the receiver’s text as RTF with attachments to a file or directory at `path`.
- [func rtfd(from: NSRange) -> Data?](nstext/rtfd(from:).md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/rtf(from:))*