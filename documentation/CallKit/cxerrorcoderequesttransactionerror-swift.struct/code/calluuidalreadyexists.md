# CXErrorCodeRequestTransactionError.Code.callUUIDAlreadyExists

**Framework**: CallKit  
**Kind**: case

The requested transaction contains call actions that reference a UUID that already exists.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case callUUIDAlreadyExists
```

## See Also

- [CXErrorCodeRequestTransactionError.Code.unknown](cxerrorcoderequesttransactionerror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeRequestTransactionError.Code.unentitled](cxerrorcoderequesttransactionerror-swift.struct/code/unentitled.md)
  The app isn’t entitled to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.unknownCallProvider](cxerrorcoderequesttransactionerror-swift.struct/code/unknowncallprovider.md)
  The controller couldn’t find a call provider to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.emptyTransaction](cxerrorcoderequesttransactionerror-swift.struct/code/emptytransaction.md)
  The requested transaction contains no actions.
- [CXErrorCodeRequestTransactionError.Code.unknownCallUUID](cxerrorcoderequesttransactionerror-swift.struct/code/unknowncalluuid.md)
  The requested transaction contains call actions that reference an unknown UUID.
- [CXErrorCodeRequestTransactionError.Code.invalidAction](cxerrorcoderequesttransactionerror-swift.struct/code/invalidaction.md)
  The requested transaction contains an invalid action.
- [CXErrorCodeRequestTransactionError.Code.maximumCallGroupsReached](cxerrorcoderequesttransactionerror-swift.struct/code/maximumcallgroupsreached.md)
  The requested transaction contains actions that, if performed, would exceed the maximum number of call groups for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/code/calluuidalreadyexists)*