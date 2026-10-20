# lockDSFID(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func lockDSFID(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func lockDSFID(requestFlags flags: NFCISO15693RequestFlag) async throws
```

```objc
- (void) lockDSFIDWithRequestFlag:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockdsfid(requestflags:completionhandler:))*