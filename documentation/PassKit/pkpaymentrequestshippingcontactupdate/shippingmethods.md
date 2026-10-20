# shippingMethods

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of shipping methods.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var shippingMethods: [PKShippingMethod] { get set }
```

```objc
@property (nonatomic, copy) NSArray<PKShippingMethod *> * shippingMethods;
```

## See Also

### Updating user errors and shipping methods
- [var errors: [any Error]!](./errors.md)
  An array of shipping contact information errors that the user must resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestshippingcontactupdate/shippingmethods)*