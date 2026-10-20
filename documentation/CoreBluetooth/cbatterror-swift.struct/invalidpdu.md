# invalidPdu

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

The attribute Protocol Data Unit (PDU) is invalid.

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
static var invalidPdu: CBATTError.Code { get }
```

## See Also

### Error Codes
- [static var success: CBATTError.Code](./success.md)
  The ATT command or request successfully completed.
- [static var invalidHandle: CBATTError.Code](./invalidhandle.md)
  The attribute handle is invalid on this peripheral.
- [static var readNotPermitted: CBATTError.Code](./readnotpermitted.md)
  The permissions prohibit reading the attribute’s value.
- [static var writeNotPermitted: CBATTError.Code](./writenotpermitted.md)
  The permissions prohibit writing the attribute’s value.
- [static var insufficientAuthentication: CBATTError.Code](./insufficientauthentication.md)
  Reading or writing the attribute’s value failed for lack of authentication.
- [static var requestNotSupported: CBATTError.Code](./requestnotsupported.md)
  The attribute server doesn’t support the request received from the client.
- [static var invalidOffset: CBATTError.Code](./invalidoffset.md)
  The specified offset value was past the end of the attribute’s value.
- [static var insufficientAuthorization: CBATTError.Code](./insufficientauthorization.md)
  Reading or writing the attribute’s value failed for lack of authorization.
- [static var prepareQueueFull: CBATTError.Code](./preparequeuefull.md)
  The prepare queue is full, as a result of there being too many write requests in the queue.
- [static var attributeNotFound: CBATTError.Code](./attributenotfound.md)
  The attribute wasn’t found within the specified attribute handle range.
- [static var attributeNotLong: CBATTError.Code](./attributenotlong.md)
  The ATT read blob request can’t read or write the attribute.
- [static var insufficientEncryptionKeySize: CBATTError.Code](./insufficientencryptionkeysize.md)
  The encryption key size used for encrypting this link is insufficient.
- [static var invalidAttributeValueLength: CBATTError.Code](./invalidattributevaluelength.md)
  The length of the attribute’s value is invalid for the intended operation.
- [static var unlikelyError: CBATTError.Code](./unlikelyerror.md)
  The ATT request encountered an unlikely error and wasn’t completed.
- [static var insufficientEncryption: CBATTError.Code](./insufficientencryption.md)
  Reading or writing the attribute’s value failed for lack of encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/invalidpdu)*