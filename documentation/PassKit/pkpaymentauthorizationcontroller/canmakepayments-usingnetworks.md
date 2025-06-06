# canMakePayments(usingNetworks:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns whether the user can make payments through the specified network.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user can make payments through any of the specified networks; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

User may not be able to make payments for a variety of reasons. For example, this functionality may not be supported by their hardware, or it may be restricted by parental controls.

If there are no configured payment cards, this method always returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `supportedNetworks`: An array of payment networks, as listed in Payment Networks.

## See Also

- [class func canMakePayments() -> Bool](pkpaymentauthorizationcontroller/canmakepayments.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:capabilities:).md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements(using:).md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment network brands.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements(using:capabilities:).md)
  Returns a Boolean value indicating whether this device can process disbursement requests using the specified payment network brands and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:))*