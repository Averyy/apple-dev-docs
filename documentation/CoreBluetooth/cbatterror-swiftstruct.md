# CBATTError

**Framework**: Core Bluetooth  
**Kind**: struct

An error that Core Bluetooth returns while using Attribute Protocol (ATT).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CBATTError
```

## Topics

### Error Codes
- [static var success: CBATTError.Code](cbatterror-swift.struct/success.md)
  The ATT command or request successfully completed.
- [static var invalidHandle: CBATTError.Code](cbatterror-swift.struct/invalidhandle.md)
  The attribute handle is invalid on this peripheral.
- [static var readNotPermitted: CBATTError.Code](cbatterror-swift.struct/readnotpermitted.md)
  The permissions prohibit reading the attribute’s value.
- [static var writeNotPermitted: CBATTError.Code](cbatterror-swift.struct/writenotpermitted.md)
  The permissions prohibit writing the attribute’s value.
- [static var invalidPdu: CBATTError.Code](cbatterror-swift.struct/invalidpdu.md)
  The attribute Protocol Data Unit (PDU) is invalid.
- [static var insufficientAuthentication: CBATTError.Code](cbatterror-swift.struct/insufficientauthentication.md)
  Reading or writing the attribute’s value failed for lack of authentication.
- [static var requestNotSupported: CBATTError.Code](cbatterror-swift.struct/requestnotsupported.md)
  The attribute server doesn’t support the request received from the client.
- [static var invalidOffset: CBATTError.Code](cbatterror-swift.struct/invalidoffset.md)
  The specified offset value was past the end of the attribute’s value.
- [static var insufficientAuthorization: CBATTError.Code](cbatterror-swift.struct/insufficientauthorization.md)
  Reading or writing the attribute’s value failed for lack of authorization.
- [static var prepareQueueFull: CBATTError.Code](cbatterror-swift.struct/preparequeuefull.md)
  The prepare queue is full, as a result of there being too many write requests in the queue.
- [static var attributeNotFound: CBATTError.Code](cbatterror-swift.struct/attributenotfound.md)
  The attribute wasn’t found within the specified attribute handle range.
- [static var attributeNotLong: CBATTError.Code](cbatterror-swift.struct/attributenotlong.md)
  The ATT read blob request can’t read or write the attribute.
- [static var insufficientEncryptionKeySize: CBATTError.Code](cbatterror-swift.struct/insufficientencryptionkeysize.md)
  The encryption key size used for encrypting this link is insufficient.
- [static var invalidAttributeValueLength: CBATTError.Code](cbatterror-swift.struct/invalidattributevaluelength.md)
  The length of the attribute’s value is invalid for the intended operation.
- [static var unlikelyError: CBATTError.Code](cbatterror-swift.struct/unlikelyerror.md)
  The ATT request encountered an unlikely error and wasn’t completed.
- [static var insufficientEncryption: CBATTError.Code](cbatterror-swift.struct/insufficientencryption.md)
  Reading or writing the attribute’s value failed for lack of encryption.
- [static var unsupportedGroupType: CBATTError.Code](cbatterror-swift.struct/unsupportedgrouptype.md)
  The attribute type isn’t a supported grouping attribute as defined by a higher-layer specification.
- [static var insufficientResources: CBATTError.Code](cbatterror-swift.struct/insufficientresources.md)
  Resources are insufficient to complete the ATT request.
### Enumerations
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
### Type Properties
- [static var errorDomain: String](cbatterror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CBError](cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- [let CBATTErrorDomain: String](cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [CBATTError.Code](cbatterror-swift.struct/code.md)
  The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct)*