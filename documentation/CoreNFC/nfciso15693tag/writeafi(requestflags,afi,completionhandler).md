# writeAFI(requestFlags:afi:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Write AFI command (0x27 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeAFI(requestFlags flags: NFCISO15693RequestFlag, afi: UInt8, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAFI(requestFlags flags: NFCISO15693RequestFlag, afi: UInt8) async throws
```

```objc
- (void) writeAFIWithRequestFlag:(NFCISO15693RequestFlag) flags afi:(uint8_t) afi completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Application Family Identifier Commands
- [func lockAFI(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./lockafi%28requestflags,completionhandler%29.md)
  Sends the Lock AFI command (0x28 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/writeafi(requestflags:afi:completionhandler:))*