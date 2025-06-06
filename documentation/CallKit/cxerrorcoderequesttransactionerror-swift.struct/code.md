# CXErrorCodeRequestTransactionError.Code

**Framework**: CallKit  
**Kind**: enum

Error codes for the CallKit error domain.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

## Topics

### Constants
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
- [CXErrorCodeRequestTransactionError.Code.callUUIDAlreadyExists](cxerrorcoderequesttransactionerror-swift.struct/code/calluuidalreadyexists.md)
  The requested transaction contains call actions that reference a UUID that already exists.
- [CXErrorCodeRequestTransactionError.Code.invalidAction](cxerrorcoderequesttransactionerror-swift.struct/code/invalidaction.md)
  The requested transaction contains an invalid action.
- [CXErrorCodeRequestTransactionError.Code.maximumCallGroupsReached](cxerrorcoderequesttransactionerror-swift.struct/code/maximumcallgroupsreached.md)
  The requested transaction contains actions that, if performed, would exceed the maximum number of call groups for the provider.
### Enumeration Cases
- [CXErrorCodeRequestTransactionError.Code.callIsProtected](cxerrorcoderequesttransactionerror-swift.struct/code/callisprotected.md)
### Initializers
- [init?(rawValue: Int)](cxerrorcoderequesttransactionerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CXErrorCodeRequestTransactionError](cxerrorcoderequesttransactionerror-swift.struct.md)
- [let CXErrorDomainRequestTransaction: String](cxerrordomainrequesttransaction.md)
  Domain for errors when requesting a transaction from a call controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/code)*