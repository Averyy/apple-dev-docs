# StoreKitError.unsupported

**Framework**: StoreKit  
**Kind**: case

The operation doesn’t support this product.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
case unsupported
```

#### Discussion

The system surfaces this error when the type that originates the request doesn’t support the operation. For example, initializing an [`AdvancedCommerceProduct`](advancedcommerceproduct.md) using the product ID of an in-app purchase that isn’t registered as a generic SKU in App Store Connect.

## See Also

- [StoreKitError.networkError(_:)](storekiterror/networkerror(_:).md)
  A network error occurred.
- [StoreKitError.systemError(_:)](storekiterror/systemerror(_:).md)
  A system error occurred.
- [StoreKitError.userCancelled](storekiterror/usercancelled.md)
  The user canceled.
- [StoreKitError.notAvailableInStorefront](storekiterror/notavailableinstorefront.md)
  The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](storekiterror/notentitled.md)
  The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](storekiterror/unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storekiterror/unsupported)*