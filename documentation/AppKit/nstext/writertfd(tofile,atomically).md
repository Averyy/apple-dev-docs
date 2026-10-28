# writeRTFD(toFile:atomically:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the receiver’s text as RTF with attachments to a file or directory at `path`.

**Availability**:
- macOS

## Declaration

```swift
func writeRTFD(toFile path: String, atomically flag: Bool) -> Bool
```

```objc
- (BOOL) writeRTFDToFile:(NSString *) path atomically:(BOOL) flag;
```

## Discussion

Returns [`true`](../../Swift/true.md) on success and [`false`](../../Swift/false.md) on failure. If `atomicFlag` is [`true`](../../Swift/true.md), attempts to write the file safely so that an existing file at `path` is not overwritten, nor does a new file at `path` actually get created, unless the write is successful.

## See Also

### Reading and writing RTF files
- [func readRTFD(fromFile: String) -> Bool](./readrtfd%28fromfile%29.md)
  Attempts to read the RTFD file at the specified path.
- [func rtfd(from: NSRange) -> Data?](./rtfd%28from%29.md)
  Returns an NSData object that contains an RTFD stream corresponding to the characters and attributes within `aRange`.
- [func rtf(from: NSRange) -> Data?](./rtf%28from%29.md)
  Returns an NSData object that contains an RTF stream corresponding to the characters and attributes within `aRange`, omitting any attachment characters and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/writertfd(tofile:atomically:))*