# CXErrorCodeRequestTransactionError.Code

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CXErrorCodeRequestTransactionError : NSInteger;
```

## Topics

### Constants
- [CXErrorCodeRequestTransactionError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [CXErrorCodeRequestTransactionError.Code.unentitled](./code/unentitled.md)
  The app isn’t entitled to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.unknownCallProvider](./code/unknowncallprovider.md)
  The controller couldn’t find a call provider to perform the actions in the requested transaction.
- [CXErrorCodeRequestTransactionError.Code.emptyTransaction](./code/emptytransaction.md)
  The requested transaction contains no actions.
- [CXErrorCodeRequestTransactionError.Code.unknownCallUUID](./code/unknowncalluuid.md)
  The requested transaction contains call actions that reference an unknown UUID.
- [CXErrorCodeRequestTransactionError.Code.callUUIDAlreadyExists](./code/calluuidalreadyexists.md)
  The requested transaction contains call actions that reference a UUID that already exists.
- [CXErrorCodeRequestTransactionError.Code.invalidAction](./code/invalidaction.md)
  The requested transaction contains an invalid action.
- [CXErrorCodeRequestTransactionError.Code.maximumCallGroupsReached](./code/maximumcallgroupsreached.md)
  The requested transaction contains actions that, if performed, would exceed the maximum number of call groups for the provider.
### Enumeration Cases
- [CXErrorCodeRequestTransactionError.Code.callIsProtected](./code/callisprotected.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct CXErrorCodeRequestTransactionError](../cxerrorcoderequesttransactionerror-swift.struct.md)
- [let CXErrorDomainRequestTransaction: String](../cxerrordomainrequesttransaction.md)
  Domain for errors when requesting a transaction from a call controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcoderequesttransactionerror-swift.struct/code)*