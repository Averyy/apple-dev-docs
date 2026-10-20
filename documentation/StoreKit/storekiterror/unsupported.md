# StoreKitError.unsupported

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The operation doesn’t support this product.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
case unsupported
```

#### Discussion

The system surfaces this error when the type that originates the request doesn’t support the operation. For example, initializing an [`AdvancedCommerceProduct`](../advancedcommerceproduct.md) using the product ID of an Apple In-App Purchase that isn’t registered as a generic SKU in App Store Connect.

## See Also

### StoreKit Error Codes
- [StoreKitError.networkError(_:)](./networkerror%28_%29.md)
  A network error occurred.
- [StoreKitError.systemError(_:)](./systemerror%28_%29.md)
  A system error occurred.
- [StoreKitError.userCancelled](./usercancelled.md)
  The user canceled.
- [StoreKitError.notAvailableInStorefront](./notavailableinstorefront.md)
  The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](./notentitled.md)
  The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](./unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storekiterror/unsupported)*