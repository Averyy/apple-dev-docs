# PaymentCardReaderStore.StoreError

**Framework**: ProximityReader  
**Kind**: enum

Values that describes errors related to the payments store.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
enum StoreError
```

## Topics

### Enumeration Cases
- [PaymentCardReaderStore.StoreError.busy](paymentcardreaderstore/storeerror/busy.md)
  The store is busy executing a previous request.
- [PaymentCardReaderStore.StoreError.networkError](paymentcardreaderstore/storeerror/networkerror.md)
  The user needs to be online to fetch or resolve a batch.
- [PaymentCardReaderStore.StoreError.notAllowed](paymentcardreaderstore/storeerror/notallowed.md)
  An error that indicates there’s an entitlement issue, an invalid application bundle, or a configuration issue.
- [PaymentCardReaderStore.StoreError.passcodeDisabled](paymentcardreaderstore/storeerror/passcodedisabled.md)
  To fetch a batch device’s passcode needs to be enabled.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchAlreadyExists](paymentcardreaderstore/storeerror/storeandforwardbatchalreadyexists.md)
  An error that indicates that a previous batch exists in the store and needs to be resolved or reset prior the current fetch batch request.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchNotFound](paymentcardreaderstore/storeerror/storeandforwardbatchnotfound.md)
  The store does not have a batch.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchSizeInvalid](paymentcardreaderstore/storeerror/storeandforwardbatchsizeinvalid.md)
  The requested batch size is invalid.
- [PaymentCardReaderStore.StoreError.storeAndForwardDeletionTokenExpired](paymentcardreaderstore/storeerror/storeandforwarddeletiontokenexpired.md)
  The token provided is expired, refresh it and try again.
- [PaymentCardReaderStore.StoreError.storeAndForwardDeletionTokenInvalid](paymentcardreaderstore/storeerror/storeandforwarddeletiontokeninvalid.md)
  The token provided is invalid, try again.
- [PaymentCardReaderStore.StoreError.storeAndForwardResultsNotFound](paymentcardreaderstore/storeerror/storeandforwardresultsnotfound.md)
  The Store and Forward store is empty.
- [PaymentCardReaderStore.StoreError.unknown(code:)](paymentcardreaderstore/storeerror/unknown(code:).md)
  An unexpected error happened, try again.
### Default Implementations
- [Error Implementations](paymentcardreaderstore/storeerror/error-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/storeerror)*