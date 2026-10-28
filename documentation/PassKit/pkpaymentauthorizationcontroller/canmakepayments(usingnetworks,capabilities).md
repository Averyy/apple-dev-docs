# canMakePayments(usingNetworks:capabilities:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns whether the user can make payments using a card from the specified network with the specified capabilities.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func canMakePayments(usingNetworks supportedNetworks: [PKPaymentNetwork], capabilities capabilties: PKMerchantCapability) -> Bool
```

```objc
+ (BOOL) canMakePaymentsUsingNetworks:(NSArray<NSString *> *) supportedNetworks capabilities:(PKMerchantCapability) capabilties;
```

## Return Value

[`true`](../../Swift/true.md), if the device supports Apple Pay and the user has added a compatible card; otherwise, [`false`](../../Swift/false.md).

## Discussion

Use this method to see whether the user can make payments using a card from one of the selected networks (for example, American Express, Discover, Mastercard, Visa, etc.) with the selected capabilities (for example, credit, debit, etc.).

> **Note**:  The earliest cards added to Apple Pay may not have credit or debit information. The API for distinguishing credit cards from debit cards is intended for European markets, where merchants often charge different rates for credit and debit purchases.

## Parameters

- `supportedNetworks`: An array of payment networks, as listed in Payment Networks.
- `capabilties`: A bitmask of capability values. For a list of possible values, see [`PKMerchantCapability`](../pkmerchantcapability.md).

## See Also

### Determining whether the user can make payments or disbursements
- [class func canMakePayments() -> Bool](./canmakepayments%28%29.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](./canmakepayments%28usingnetworks%29.md)
  Returns whether the user can make payments through the specified network.
- [class func supportsDisbursements() -> Bool](./supportsdisbursements%28%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](./supportsdisbursements%28using%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment network brands.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./supportsdisbursements%28using,capabilities%29.md)
  Returns a Boolean value indicating whether this device can process disbursement requests using the specified payment network brands and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/canmakepayments(usingnetworks:capabilities:))*