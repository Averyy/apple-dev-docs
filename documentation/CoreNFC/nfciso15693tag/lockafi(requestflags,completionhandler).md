# lockAFI(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Lock AFI command (0x28 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func lockAFI(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func lockAFI(requestFlags flags: NFCISO15693RequestFlag) async throws
```

```objc
- (void) lockAFIWithRequestFlag:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Application Family Identifier Commands
- [func writeAFI(requestFlags: NFCISO15693RequestFlag, afi: UInt8, completionHandler: ((any Error)?) -> Void)](./writeafi%28requestflags,afi,completionhandler%29.md)
  Sends the Write AFI command (0x27 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockafi(requestflags:completionhandler:))*