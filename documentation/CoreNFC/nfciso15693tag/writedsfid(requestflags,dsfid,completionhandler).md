# writeDSFID(requestFlags:dsfid:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Write DSFID command (0x29 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeDSFID(requestFlags flags: NFCISO15693RequestFlag, dsfid: UInt8, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeDSFID(requestFlags flags: NFCISO15693RequestFlag, dsfid: UInt8) async throws
```

```objc
- (void) writeDSFIDWithRequestFlag:(NFCISO15693RequestFlag) flags dsfid:(uint8_t) dsfid completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Data Storage Format Identifier Commands
- [func lockDFSID(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./lockdfsid%28requestflags,completionhandler%29.md)
  Sends the Lock DSFID command (0x2A command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/writedsfid(requestflags:dsfid:completionhandler:))*