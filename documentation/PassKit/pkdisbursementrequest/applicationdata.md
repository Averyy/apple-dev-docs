# applicationData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

Optional merchant-supplied information about the disbursement request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var applicationData: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * applicationData;
```

#### Discussion

The system hashes the data and includes it in the resulting [`PKPaymentToken`](../pkpaymenttoken.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/applicationdata)*