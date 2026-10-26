# createMatchingDictionaryWithVendorID:productID:bcdDevice:interfaceNumber:configurationValue:interfaceClass:interfaceSubclass:interfaceProtocol:speed:productIDArray:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Type Method

Creates a matching dictionary to find a USB interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
+ (CFMutableDictionaryRef) createMatchingDictionaryWithVendorID:(NSNumber *) vendorID productID:(NSNumber *) productID bcdDevice:(NSNumber *) bcdDevice interfaceNumber:(NSNumber *) interfaceNumber configurationValue:(NSNumber *) configurationValue interfaceClass:(NSNumber *) interfaceClass interfaceSubclass:(NSNumber *) interfaceSubclass interfaceProtocol:(NSNumber *) interfaceProtocol speed:(NSNumber *) speed productIDArray:(NSArray *) productIDArray;
```

#### Return Value

Returns the [`CFMutableDictionary`](../../CoreFoundation/cfmutabledictionary.md) used with IOKit matching methods such as [`IOServiceGetMatchingService(_:_:)`](../../iokit/api-1514535-ioservicegetmatchingservice.md). The caller is responsible for releasing the reference.

#### Discussion

The table below shows the keys you can use to make a successful matching dictionary. A plus sign (+) separates the keys to emphasize the requirement that all of the specified keys combine.

The table presents the keys in order of specificity. The first key defines the most specific search, and the last key defines the broadest search.

| Keys | Notes |
| --- | --- |
| `idVendor` + `idProduct` + `bcdDevice` + `bConfigurationValue` + `bInterfaceNumber` | None. |
| `idVendor` + `idProduct` + `bConfigurationValue` + `bInterfaceNumber` | None. |
| `idVendor` + `bInterfaceSubClass` + `bInterfaceProtocol` | Use these keys only if `bInterfaceClass` is set to `0xFF`. |
| `idVendor` + `bInterfaceSubClass` | Use these keys only if `bInterfaceSubClass` is set to `0xFF`. |
| `bInterfaceClass` + `bInterfaceSubClass` + `bInterfaceProtocol` | Use these keys only if `bInterfaceSubClass` is not set to `0xFF`. |
| `bInterfaceClass` + `bInterfaceSubClass` | Use these keys only if `bInterfaceSubClass` is not set to `0xFF`. |

## Parameters

- `vendorID`: The vendor ID for the device you’re searching for.
- `productID`: The product ID for the device you’re searching for.
- `bcdDevice`: The release number of the device you’re searching for.
- `interfaceNumber`: The interface number of the device you’re searching for.
- `configurationValue`: The configuration value of the device you’re searching for.
- `interfaceClass`: The interface class of the device you’re searching for.
- `interfaceSubclass`: The interface subclass of the device you’re searching for.
- `interfaceProtocol`: The interface protocol of the device you’re searching for.
- `speed`: The enumeration speed of the device. You can add the speed to any of the keys in the table below.
- `productIDArray`: An array of product IDs to match against. Don’t use this parameter with the `productID` parameter.

## Topics

### Matching Properties
- [struct IOUSBHostMatchingPropertyKey](../iousbhostmatchingpropertykey.md)
  Properties for implementing the matching service.
- [typealias IOUSBHostPropertyKey](../iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.

## See Also

### Related Documentation
- [class IOUSBHostInterface](../iousbhostinterface.md)
  The class for accessing USB-related services.
- [IOUSBInterfaceDescriptor](../../iokit/iousbinterfacedescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/creatematchingdictionarywithvendorid:productid:bcddevice:interfacenumber:configurationvalue:interfaceclass:interfacesubclass:interfaceprotocol:speed:productidarray:)*