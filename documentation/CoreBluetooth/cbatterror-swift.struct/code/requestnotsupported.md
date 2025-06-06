# CBATTError.Code.requestNotSupported

**Framework**: Core Bluetooth  
**Kind**: case

The attribute server doesn’t support the request received from the client.

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
case requestNotSupported
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/code/requestnotsupported)*