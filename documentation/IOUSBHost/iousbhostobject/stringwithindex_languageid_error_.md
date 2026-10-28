# stringWithIndex:languageID:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Retrieves a string from a string descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (const NSString *) stringWithIndex:(NSUInteger) index languageID:(NSUInteger) languageID error:(NSError **) error;
```

## Return Value

The string from the specified string descriptor.

## Parameters

- `index`: The descriptor index value that is the low byte of `wValue` of the `SET_DESCRIPTOR` control request (See USB 3.2, 9.4.8.).
- `languageID`: A descriptor language ID that is the `wIndex` of the `SET_DESCRIPTOR` control request (See USB 3.2, 9.4.8.). The default value is [`kIOUSBLanguageIDEnglishUS`](../../iokit/tiousblanguageid/kiousblanguageidenglishus.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Retrieving Base Class Descriptors
- [Parsing USB Descriptors](../parsing-usb-descriptors.md)
  Extract information from various USB descriptors using helper methods.
- [- descriptorWithType:length:index:languageID:requestType:requestRecipient:error:](./descriptorwithtype_length_index_languageid_requesttype_requestrecipient_error_.md)
  Retrieves a descriptor from the cache or the device.
- [- descriptorWithType:length:error:](./descriptorwithtype_length_error_.md)
  Retrieves a descriptor with default arguments from the cache or the device.
- [- descriptorWithType:length:index:languageID:error:](./descriptorwithtype_length_index_languageid_error_.md)
  Retrieves a string descriptor from the cache or the device.
- [- stringWithIndex:error:](./stringwithindex_error_.md)
  Retrieves an English-language string from a string descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/stringwithindex:languageid:error:)*