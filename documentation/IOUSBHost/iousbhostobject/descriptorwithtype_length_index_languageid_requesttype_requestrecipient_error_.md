# descriptorWithType:length:index:languageID:requestType:requestRecipient:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Retrieves a descriptor from the cache or the device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (const IOUSBDescriptor *) descriptorWithType:(tIOUSBDescriptorType) type length:(NSUInteger *) length index:(NSUInteger) index languageID:(NSUInteger) languageID requestType:(tIOUSBDeviceRequestTypeValue) requestType requestRecipient:(tIOUSBDeviceRequestRecipientValue) requestRecipient error:(NSError **) error;
```

## Return Value

A pointer to the cached descriptor, or `nil` if no matching descriptor returns.

## Discussion

This method searches the descriptor cache for the descriptor that matches the input arguments. If the descriptor isn’t in the cache, the method issues a `GET_DESCRIPTOR` control request (See USB 3.2, 9.4.3.) to retrieve the descriptor from the device. If the device request is successful, the method adds the retrieved descriptor to the cache.

## Parameters

- `type`: The type of the descriptor to find.
- `length`: A reference to an [`NSUInteger`](../../ObjectiveC/nsuinteger.md) that updates with the length of the descriptor. You can use `wLength` when searching for variable-length configuration or BOS descriptors, or when searching for nonstandard descriptor types.
- `index`: A descriptor index value that is the low byte of `wValue` of the `SET_DESCRIPTOR` control request (See USB 3.2, 9.4.8.). The default is value is `0`.
- `languageID`: A descriptor language ID that’s the `wIndex` of the `SET_DESCRIPTOR` control request (See USB 3.2, 9.4.8.). The default value is `0`.
- `requestType`: The request type for a `GET_DESCRIPTOR` control request. The default value is [`kIOUSBDeviceRequestTypeValueStandard`](../../iokit/tiousbdevicerequesttypevalue/kiousbdevicerequesttypevaluestandard.md).
- `requestRecipient`: The request recipient for a `GET_DESCRIPTOR` control request. The default value is [`kIOUSBDeviceRequestRecipientValueDevice`](../../iokit/tiousbdevicerequestrecipientvalue/kiousbdevicerequestrecipientvaluedevice.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Retrieving Base Class Descriptors
- [Parsing USB Descriptors](../parsing-usb-descriptors.md)
  Extract information from various USB descriptors using helper methods.
- [- descriptorWithType:length:error:](./descriptorwithtype_length_error_.md)
  Retrieves a descriptor with default arguments from the cache or the device.
- [- descriptorWithType:length:index:languageID:error:](./descriptorwithtype_length_index_languageid_error_.md)
  Retrieves a string descriptor from the cache or the device.
- [- stringWithIndex:languageID:error:](./stringwithindex_languageid_error_.md)
  Retrieves a string from a string descriptor.
- [- stringWithIndex:error:](./stringwithindex_error_.md)
  Retrieves an English-language string from a string descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/descriptorwithtype:length:index:languageid:requesttype:requestrecipient:error:)*