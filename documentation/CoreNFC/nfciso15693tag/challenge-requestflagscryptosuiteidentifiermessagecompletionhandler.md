# challenge(requestFlags:cryptoSuiteIdentifier:message:completionHandler:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@preconcurrency
func challenge(requestFlags flags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/challenge(requestflags:cryptosuiteidentifier:message:completionhandler:))*