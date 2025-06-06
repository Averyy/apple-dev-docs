# SecTrustSetOptions(_:_:)

**Framework**: Security  
**Kind**: func

Sets option flags for customizing evaluation of a trust object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTrustSetOptions(_ trustRef: SecTrust, _ options: SecTrustOptionFlags) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `trustRef`: The trust object to modify.
- `options`: The new set of option flags. For a list of options, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetoptions(_:_:))*