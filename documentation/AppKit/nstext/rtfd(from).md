# rtfd(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.

**Availability**:
- macOS

## Declaration

```swift
func rtfd(from range: NSRange) -> Data?
```

```objc
- (NSData *) RTFDFromRange:(NSRange) range;
```

#### Discussion

Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the NSData object as the first argument to `NSPasteboard`’s [`setData(_:forType:)`](../nspasteboard/setdata%28_,fortype%29.md) method, with a second argument of `NSRTFDPboardType`.

## See Also

### Reading and writing RTF files
- [func readRTFD(fromFile: String) -> Bool](./readrtfd%28fromfile%29.md)
  Attempts to read the RTFD file at the specified path.
- [func writeRTFD(toFile: String, atomically: Bool) -> Bool](./writertfd%28tofile,atomically%29.md)
  Writes the receiver’s text as RTF with attachments to a file or directory at `path`.
- [func rtf(from: NSRange) -> Data?](./rtf%28from%29.md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/rtfd(from:))*