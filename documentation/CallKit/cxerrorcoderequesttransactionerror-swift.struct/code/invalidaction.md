# CXErrorCodeRequestTransactionError.Code.invalidAction

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

The requested transaction contains an invalid action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case invalidAction
```

```c
CXErrorCodeRequestTransactionErrorInvalidAction
```

## See Also

### Constants
- [CXErrorCodeRequestTransactionError.Code.unknown](./unknown.md)
  An unknown error occurred.
- [CXErrorCodeRequestTransactionError.Code.unentitled](./unentitled.md)
  The app isn’t entitled to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.unknownCallProvider](./unknowncallprovider.md)
  The controller couldn’t find a call provider to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.emptyTransaction](./emptytransaction.md)
  The requested transaction contains no actions.
- [CXErrorCodeRequestTransactionError.Code.unknownCallUUID](./unknowncalluuid.md)
  The requested transaction contains call actions that reference an unknown UUID.
- [CXErrorCodeRequestTransactionError.Code.callUUIDAlreadyExists](./calluuidalreadyexists.md)
  The requested transaction contains call actions that reference a UUID that already exists.
- [CXErrorCodeRequestTransactionError.Code.maximumCallGroupsReached](./maximumcallgroupsreached.md)
  The requested transaction contains actions that, if performed, would exceed the maximum number of call groups for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/code/invalidaction)*