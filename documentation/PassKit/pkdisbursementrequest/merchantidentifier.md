# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A string that identifies the merchant.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var merchantIdentifier: String { get set }
```

```objc
@property (nonatomic, copy) NSString * merchantIdentifier;
```

#### Discussion

This string needs to match one of the merchant IDs you registered with the Developer Portal or in Xcode, which the [`Merchant IDs Entitlement`](../../BundleResources/entitlements/com.apple.developer.in-app-payments.md) specifies in the app’s entitlements. For more information on adding merchant IDs, see [Configure Apple Pay (iOS, watchOS)](https://help.apple.com/xcode/mac/current/#/deva43983eb7?sub=dev171483d6e).

## See Also

### Setting the merchant information
- [var merchantCapabilities: PKMerchantCapability](./merchantcapabilities.md)
  A value that represents the payment-processing capabilities of the merchant.
- [var supportedNetworks: [PKPaymentNetwork]](./supportednetworks.md)
  An array of payment networks the merchant supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/merchantidentifier)*