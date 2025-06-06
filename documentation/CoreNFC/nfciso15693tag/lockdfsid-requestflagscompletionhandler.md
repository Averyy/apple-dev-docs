# lockDFSID(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Lock DSFID command (0x2A command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func lockDFSID(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping ((any Error)?) -> Void)
```

## See Also

- [func writeDSFID(requestFlags: NFCISO15693RequestFlag, dsfid: UInt8, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writedsfid(requestflags:dsfid:completionhandler:).md)
  Sends the Write DSFID command (0x29 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockdfsid(requestflags:completionhandler:))*