# authenticate(requestFlags:cryptoSuiteIdentifier:message:)

**Framework**: Core NFC  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+

## Declaration

```swift
func authenticate(requestFlags flags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data) async throws -> (NFCISO15693ResponseFlag, Data)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/authenticate(requestflags:cryptosuiteidentifier:message:))*