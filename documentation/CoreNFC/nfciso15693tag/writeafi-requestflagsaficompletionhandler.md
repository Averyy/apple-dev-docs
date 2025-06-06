# writeAFI(requestFlags:afi:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Write AFI command (0x27 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeAFI(requestFlags flags: NFCISO15693RequestFlag, afi: UInt8) async throws
```

## See Also

- [func lockAFI(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockafi(requestflags:completionhandler:).md)
  Sends the Lock AFI command (0x28 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/writeafi(requestflags:afi:completionhandler:))*