# lockDFSID(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Lock DSFID command (0x2A command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
func lockDFSID(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping ((any Error)?) -> Void)
```

```objc
- (void) lockDFSIDWithRequestFlag:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Data Storage Format Identifier Commands
- [func writeDSFID(requestFlags: NFCISO15693RequestFlag, dsfid: UInt8, completionHandler: ((any Error)?) -> Void)](./writedsfid%28requestflags,dsfid,completionhandler%29.md)
  Sends the Write DSFID command (0x29 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockdfsid(requestflags:completionhandler:))*