# CBATTError.Code

**Framework**: Core Bluetooth  
**Kind**: enum

The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.

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
enum Code
```

#### Overview

These error constants derive from the Bluetooth ATT error codes, defined in the Bluetooth 4.0 specification. For more information, see the Bluetooth 4.0 specification, Volume 3, Part F, Section 3.4.1.1.

## Topics

### Error Codes
- [CBATTError.Code.success](cbatterror-swift.struct/code/success.md)
  The ATT command or request successfully completed.
- [CBATTError.Code.invalidHandle](cbatterror-swift.struct/code/invalidhandle.md)
  The attribute handle is invalid on this peripheral.
- [CBATTError.Code.readNotPermitted](cbatterror-swift.struct/code/readnotpermitted.md)
  The permissions prohibit reading the attribute’s value.
- [CBATTError.Code.writeNotPermitted](cbatterror-swift.struct/code/writenotpermitted.md)
  The permissions prohibit writing the attribute’s value.
- [CBATTError.Code.invalidPdu](cbatterror-swift.struct/code/invalidpdu.md)
  The attribute Protocol Data Unit (PDU) is invalid.
- [CBATTError.Code.insufficientAuthentication](cbatterror-swift.struct/code/insufficientauthentication.md)
  Reading or writing the attribute’s value failed for lack of authentication.
- [CBATTError.Code.requestNotSupported](cbatterror-swift.struct/code/requestnotsupported.md)
  The attribute server doesn’t support the request received from the client.
- [CBATTError.Code.invalidOffset](cbatterror-swift.struct/code/invalidoffset.md)
  The specified offset value was past the end of the attribute’s value.
- [CBATTError.Code.insufficientAuthorization](cbatterror-swift.struct/code/insufficientauthorization.md)
  Reading or writing the attribute’s value failed for lack of authorization.
- [CBATTError.Code.prepareQueueFull](cbatterror-swift.struct/code/preparequeuefull.md)
  The prepare queue is full, as a result of there being too many write requests in the queue.
- [CBATTError.Code.attributeNotFound](cbatterror-swift.struct/code/attributenotfound.md)
  The attribute wasn’t found within the specified attribute handle range.
- [CBATTError.Code.attributeNotLong](cbatterror-swift.struct/code/attributenotlong.md)
  The ATT read blob request can’t read or write the attribute.
- [CBATTError.Code.insufficientEncryptionKeySize](cbatterror-swift.struct/code/insufficientencryptionkeysize.md)
  The encryption key size used for encrypting this link is insufficient.
- [CBATTError.Code.invalidAttributeValueLength](cbatterror-swift.struct/code/invalidattributevaluelength.md)
  The length of the attribute’s value is invalid for the intended operation.
- [CBATTError.Code.unlikelyError](cbatterror-swift.struct/code/unlikelyerror.md)
  The ATT request encountered an unlikely error and wasn’t completed.
- [CBATTError.Code.insufficientEncryption](cbatterror-swift.struct/code/insufficientencryption.md)
  Reading or writing the attribute’s value failed for lack of encryption.
- [CBATTError.Code.unsupportedGroupType](cbatterror-swift.struct/code/unsupportedgrouptype.md)
  The attribute type isn’t a supported grouping attribute as defined by a higher-layer specification.
- [CBATTError.Code.insufficientResources](cbatterror-swift.struct/code/insufficientresources.md)
  Resources are insufficient to complete the ATT request.
### Initializers
- [init?(rawValue: Int)](cbatterror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CBError](cberror-swift.struct.md)
  An error that Core Bluetooth returns during Bluetooth transactions.
- [let CBErrorDomain: String](cberrordomain.md)
  The domain for Core Bluetooth errors.
- [CBError.Code](cberror-swift.struct/code.md)
  The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- [let CBATTErrorDomain: String](cbatterrordomain.md)
  The domain for Core Bluetooth ATT errors.
- [struct CBATTError](cbatterror-swift.struct.md)
  An error that Core Bluetooth returns while using Attribute Protocol (ATT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/code)*