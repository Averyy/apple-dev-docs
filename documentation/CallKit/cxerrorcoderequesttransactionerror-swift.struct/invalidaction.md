# invalidAction

**Framework**: CallKit  
**Kind**: property

The requested transaction contains an invalid action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var invalidAction: CXErrorCodeRequestTransactionError.Code { get }
```

## See Also

- [static var unknown: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/unknown.md)
  An unknown error occurred.
- [static var unentitled: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/unentitled.md)
  The app doesn’t have the entitlement to perform the actions in the requested transaction.
- [static var unknownCallProvider: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/unknowncallprovider.md)
  The controller can’t find a call provider to perform the actions in the requested transaction.
- [static var emptyTransaction: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/emptytransaction.md)
  The requested transaction doesn’t contain any actions.
- [static var unknownCallUUID: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/unknowncalluuid.md)
  The requested transaction contains call actions that reference an unknown UUID.
- [static var callUUIDAlreadyExists: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/calluuidalreadyexists.md)
  The requested transaction contains call actions that reference a UUID that already exists.
- [static var maximumCallGroupsReached: CXErrorCodeRequestTransactionError.Code](cxerrorcoderequesttransactionerror-swift.struct/maximumcallgroupsreached.md)
  Performing the requested transaction exceeds the maximum number of call groups for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/invalidaction)*