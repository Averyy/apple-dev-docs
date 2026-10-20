# resetToReady(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Reset To Ready command (0x26 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func resetToReady(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func resetToReady(requestFlags flags: NFCISO15693RequestFlag) async throws
```

```objc
- (void) resetToReadyWithRequestFlags:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/resettoready(requestflags:completionhandler:))*