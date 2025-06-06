# StoreKitError.systemError(_:)

**Framework**: StoreKit  
**Kind**: case

A system error occurred.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case systemError(any Error)
```

## See Also

- [StoreKitError.networkError(_:)](storekiterror/networkerror(_:).md)
  A network error occurred.
- [StoreKitError.userCancelled](storekiterror/usercancelled.md)
  The user canceled.
- [StoreKitError.notAvailableInStorefront](storekiterror/notavailableinstorefront.md)
  The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](storekiterror/notentitled.md)
  The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](storekiterror/unknown.md)
  An unknown error occurred.
- [StoreKitError.unsupported](storekiterror/unsupported.md)
  The operation doesn’t support this product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storekiterror/systemerror(_:))*