# errors

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of payment-method errors that the user must resolve.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var errors: [any Error]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<NSError *> * errors;
```

#### Discussion


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestpaymentmethodupdate/errors)*