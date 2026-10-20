# unentitled

**Framework**: CallKit  
**Kind**: property  
**Role**: Type Property

The app doesn’t have the entitlement to perform the actions in the requested transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var unentitled: CXErrorCodeRequestTransactionError.Code { get }
```

## See Also

### Constants
- [static var unknown: CXErrorCodeRequestTransactionError.Code](./unknown.md)
  An unknown error occurred.
- [static var unknownCallProvider: CXErrorCodeRequestTransactionError.Code](./unknowncallprovider.md)
  The controller can’t find a call provider to perform the actions in the requested transaction.
- [static var emptyTransaction: CXErrorCodeRequestTransactionError.Code](./emptytransaction.md)
  The requested transaction doesn’t contain any actions.
- [static var unknownCallUUID: CXErrorCodeRequestTransactionError.Code](./unknowncalluuid.md)
  The requested transaction contains call actions that reference an unknown UUID.
- [static var callUUIDAlreadyExists: CXErrorCodeRequestTransactionError.Code](./calluuidalreadyexists.md)
  The requested transaction contains call actions that reference a UUID that already exists.
- [static var invalidAction: CXErrorCodeRequestTransactionError.Code](./invalidaction.md)
  The requested transaction contains an invalid action.
- [static var maximumCallGroupsReached: CXErrorCodeRequestTransactionError.Code](./maximumcallgroupsreached.md)
  Performing the requested transaction exceeds the maximum number of call groups for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/unentitled)*