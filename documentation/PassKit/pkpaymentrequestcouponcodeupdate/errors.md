# errors

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of errors for the coupon code that the user must resolve.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var errors: [any Error]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<NSError *> * errors;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestcouponcodeupdate/errors)*