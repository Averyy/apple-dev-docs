# status

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Payment authorization general status.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var status: PKPaymentAuthorizationStatus { get set }
```

#### Discussion

See [`PKPaymentAuthorizationStatus`](pkpaymentauthorizationstatus.md) for the list of status values.

## See Also

- [var errors: [any Error]!](pkpaymentauthorizationresult/errors.md)
  List of errors in the Apple Pay sheet.
- [enum PKPaymentAuthorizationStatus](pkpaymentauthorizationstatus.md)
  General success and failure status for payment authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult/status)*