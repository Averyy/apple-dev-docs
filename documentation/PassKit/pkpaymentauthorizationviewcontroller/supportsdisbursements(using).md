# supportsDisbursements(using:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class func supportsDisbursements(using supportedNetworks: [PKPaymentNetwork]) -> Bool
```

```objc
+ (BOOL) supportsDisbursementsUsingNetworks:(NSArray<NSString *> *) supportedNetworks;
```

## Return Value

[`true`](../../Swift/true.md) if the device can process disbursement requests using the specified payment networks; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `supportedNetworks`: An array of payment networks to check.

## See Also

### Determining whether the user can make payments
- [class func canMakePayments() -> Bool](./canmakepayments%28%29.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](./canmakepayments%28usingnetworks%29.md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./canmakepayments%28usingnetworks,capabilities%29.md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](./supportsdisbursements%28%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./supportsdisbursements%28using,capabilities%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks and merchant capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/supportsdisbursements(using:))*