# PaymentCardReaderStore.StoreError

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Values that describes errors related to the payments store.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
enum StoreError
```

## Topics

### Enumeration Cases
- [PaymentCardReaderStore.StoreError.busy](./storeerror/busy.md)
  The store is busy executing a previous request.
- [PaymentCardReaderStore.StoreError.networkError](./storeerror/networkerror.md)
  The user needs to be online to fetch or resolve a batch.
- [PaymentCardReaderStore.StoreError.notAllowed](./storeerror/notallowed.md)
  An error that indicates there’s an entitlement issue, an invalid application bundle, or a configuration issue.
- [PaymentCardReaderStore.StoreError.passcodeDisabled](./storeerror/passcodedisabled.md)
  To fetch a batch device’s passcode needs to be enabled.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchAlreadyExists](./storeerror/storeandforwardbatchalreadyexists.md)
  An error that indicates that a previous batch exists in the store and needs to be resolved or reset prior the current fetch batch request.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchNotFound](./storeerror/storeandforwardbatchnotfound.md)
  The store does not have a batch.
- [PaymentCardReaderStore.StoreError.storeAndForwardBatchSizeInvalid](./storeerror/storeandforwardbatchsizeinvalid.md)
  The requested batch size is invalid.
- [PaymentCardReaderStore.StoreError.storeAndForwardDeletionTokenExpired](./storeerror/storeandforwarddeletiontokenexpired.md)
  The token provided is expired, refresh it and try again.
- [PaymentCardReaderStore.StoreError.storeAndForwardDeletionTokenInvalid](./storeerror/storeandforwarddeletiontokeninvalid.md)
  The token provided is invalid, try again.
- [PaymentCardReaderStore.StoreError.storeAndForwardResultsNotFound](./storeerror/storeandforwardresultsnotfound.md)
  The Store and Forward store is empty.
- [PaymentCardReaderStore.StoreError.unknown(code:)](./storeerror/unknown%28code%29.md)
  An unexpected error happened, try again.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore/storeerror)*