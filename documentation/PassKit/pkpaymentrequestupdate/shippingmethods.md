# shippingMethods

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The list of shipping methods available for a payment request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var shippingMethods: [PKShippingMethod] { get set }
```

```objc
@property (nonatomic, copy) NSArray<PKShippingMethod *> * shippingMethods;
```

#### Discussion

The default value is an empty array that indicates there’s no update to the shipping methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestupdate/shippingmethods)*