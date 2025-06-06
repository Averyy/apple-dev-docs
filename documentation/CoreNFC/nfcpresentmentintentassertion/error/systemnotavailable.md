# NFCPresentmentIntentAssertion.Error.systemNotAvailable

**Framework**: Core NFC  
**Kind**: case

The system is unavailable because it’s in the cool-down period.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case systemNotAvailable
```

#### Discussion

CoreNFC enforces a cool-down period after one [`NFCPresentmentIntentAssertion`](nfcpresentmentintentassertion.md) invalidates and before you can acquire another one. If you receive this error, wait a short time before trying to acquire a new [`NFCPresentmentIntentAssertion`](nfcpresentmentintentassertion.md).

## See Also

- [NFCPresentmentIntentAssertion.Error.systemEligibilityFailed](nfcpresentmentintentassertion/error/systemeligibilityfailed.md)
  The current system isn’t eligible to use this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion/error/systemnotavailable)*