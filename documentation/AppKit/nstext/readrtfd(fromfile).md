# readRTFD(fromFile:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to read the RTFD file at the specified path.

**Availability**:
- macOS

## Declaration

```swift
func readRTFD(fromFile path: String) -> Bool
```

```objc
- (BOOL) readRTFDFromFile:(NSString *) path;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

`path` should be the path for an `.rtf` file or an `.rtfd` file wrapper, not for the RTF file within an `.rtfd` file wrapper.

## See Also

### Reading and writing RTF files
- [func writeRTFD(toFile: String, atomically: Bool) -> Bool](./writertfd%28tofile,atomically%29.md)
  Writes the receiver’s text as RTF with attachments to a file or directory at `path`.
- [func rtfd(from: NSRange) -> Data?](./rtfd%28from%29.md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.
- [func rtf(from: NSRange) -> Data?](./rtf%28from%29.md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/readrtfd(fromfile:))*