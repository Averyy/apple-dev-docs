# StoreKitError

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

StoreKit Apple In-App Purchase error codes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum StoreKitError
```

## Topics

### StoreKit Error Codes
- [StoreKitError.networkError(_:)](./storekiterror/networkerror%28_%29.md)
  A network error occurred.
- [StoreKitError.systemError(_:)](./storekiterror/systemerror%28_%29.md)
  A system error occurred.
- [StoreKitError.userCancelled](./storekiterror/usercancelled.md)
  The user canceled.
- [StoreKitError.notAvailableInStorefront](./storekiterror/notavailableinstorefront.md)
  The function isn’t available on devices configured for this storefront.
- [StoreKitError.notEntitled](./storekiterror/notentitled.md)
  The app doesn’t have the appropriate entitlements to use the functionality.
- [StoreKitError.unknown](./storekiterror/unknown.md)
  An unknown error occurred.
- [StoreKitError.unsupported](./storekiterror/unsupported.md)
  The operation doesn’t support this product.
### Enumeration Cases
- [StoreKitError.invalidPresentationContext](./storekiterror/invalidpresentationcontext.md)
  StoreKit UI cannot be presented from the current context.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storekiterror)*