# canMakePayments()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns whether the user can make payments.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func canMakePayments() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports making payments; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

User may not be able to make payments for a variety of reasons. For example, this functionality may not be supported by their hardware, or it may be restricted by parental controls.

On devices that support making payments but don’t have any payment cards configured, the [`present(completion:)`](pkpaymentauthorizationcontroller/present(completion:).md) method returns [`true`](https://developer.apple.com/documentation/Swift/true) because the hardware and parental controls allow making payments, but the [`canMakePayments(usingNetworks:)`](pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:).md) method returns [`false`](https://developer.apple.com/documentation/Swift/false) regardless of network.

## See Also

- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:).md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:capabilities:).md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements(using:).md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment network brands.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationcontroller/supportsdisbursements(using:capabilities:).md)
  Returns a Boolean value indicating whether this device can process disbursement requests using the specified payment network brands and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/canmakepayments())*