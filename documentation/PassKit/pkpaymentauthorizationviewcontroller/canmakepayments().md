# canMakePayments()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns whether the user can make payments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class func canMakePayments() -> Bool
```

```objc
+ (BOOL) canMakePayments;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports making payments; otherwise, [`false`](../../Swift/false.md).

## Discussion

User may not be able to make payments for a variety of reasons. For example, this functionality may not be supported by their hardware, or it may be restricted by parental controls.

On devices that support making payments but don’t have any payment cards configured, the [`canMakePayments()`](./canmakepayments%28%29.md) method returns [`true`](../../Swift/true.md) because the hardware and parental controls allow making payments, but the [`canMakePayments(usingNetworks:)`](./canmakepayments%28usingnetworks%29.md) method returns [`false`](../../Swift/false.md) regardless of network.

## See Also

### Determining whether the user can make payments
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](./canmakepayments%28usingnetworks%29.md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./canmakepayments%28usingnetworks,capabilities%29.md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](./supportsdisbursements%28%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](./supportsdisbursements%28using%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./supportsdisbursements%28using,capabilities%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks and merchant capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/canmakepayments())*