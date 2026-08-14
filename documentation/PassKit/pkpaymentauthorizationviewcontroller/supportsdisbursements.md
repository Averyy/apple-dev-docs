# supportsDisbursements()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether this device can process disbursement requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class func supportsDisbursements() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device can process disbursement requests; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [class func canMakePayments() -> Bool](pkpaymentauthorizationviewcontroller/canmakepayments.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](pkpaymentauthorizationviewcontroller/canmakepayments(usingnetworks:).md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationviewcontroller/canmakepayments(usingnetworks:capabilities:).md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](pkpaymentauthorizationviewcontroller/supportsdisbursements(using:).md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](pkpaymentauthorizationviewcontroller/supportsdisbursements(using:capabilities:).md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks and merchant capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/supportsdisbursements())*