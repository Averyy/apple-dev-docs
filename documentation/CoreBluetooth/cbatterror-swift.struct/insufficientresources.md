# insufficientResources

**Framework**: Core Bluetooth  
**Kind**: property

Resources are insufficient to complete the ATT request.

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
static var insufficientResources: CBATTError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/insufficientresources)*