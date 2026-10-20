# CBATTError.Code.success

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

The ATT command or request successfully completed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case success
```

```c
CBATTErrorSuccess
```

## See Also

### Error Codes
- [CBATTError.Code.invalidHandle](./invalidhandle.md)
  The attribute handle is invalid on this peripheral.
- [CBATTError.Code.readNotPermitted](./readnotpermitted.md)
  The permissions prohibit reading the attribute’s value.
- [CBATTError.Code.writeNotPermitted](./writenotpermitted.md)
  The permissions prohibit writing the attribute’s value.
- [CBATTError.Code.invalidPdu](./invalidpdu.md)
  The attribute Protocol Data Unit (PDU) is invalid.
- [CBATTError.Code.insufficientAuthentication](./insufficientauthentication.md)
  Reading or writing the attribute’s value failed for lack of authentication.
- [CBATTError.Code.requestNotSupported](./requestnotsupported.md)
  The attribute server doesn’t support the request received from the client.
- [CBATTError.Code.invalidOffset](./invalidoffset.md)
  The specified offset value was past the end of the attribute’s value.
- [CBATTError.Code.insufficientAuthorization](./insufficientauthorization.md)
  Reading or writing the attribute’s value failed for lack of authorization.
- [CBATTError.Code.prepareQueueFull](./preparequeuefull.md)
  The prepare queue is full, as a result of there being too many write requests in the queue.
- [CBATTError.Code.attributeNotFound](./attributenotfound.md)
  The attribute wasn’t found within the specified attribute handle range.
- [CBATTError.Code.attributeNotLong](./attributenotlong.md)
  The ATT read blob request can’t read or write the attribute.
- [CBATTError.Code.insufficientEncryptionKeySize](./insufficientencryptionkeysize.md)
  The encryption key size used for encrypting this link is insufficient.
- [CBATTError.Code.invalidAttributeValueLength](./invalidattributevaluelength.md)
  The length of the attribute’s value is invalid for the intended operation.
- [CBATTError.Code.unlikelyError](./unlikelyerror.md)
  The ATT request encountered an unlikely error and wasn’t completed.
- [CBATTError.Code.insufficientEncryption](./insufficientencryption.md)
  Reading or writing the attribute’s value failed for lack of encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/code/success)*