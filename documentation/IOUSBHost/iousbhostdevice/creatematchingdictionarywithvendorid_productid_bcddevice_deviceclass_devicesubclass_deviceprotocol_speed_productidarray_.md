# createMatchingDictionaryWithVendorID:productID:bcdDevice:deviceClass:deviceSubclass:deviceProtocol:speed:productIDArray:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Type Method

Creates a matching dictionary to find a USB device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
+ (CFMutableDictionaryRef) createMatchingDictionaryWithVendorID:(NSNumber *) vendorID productID:(NSNumber *) productID bcdDevice:(NSNumber *) bcdDevice deviceClass:(NSNumber *) deviceClass deviceSubclass:(NSNumber *) deviceSubclass deviceProtocol:(NSNumber *) deviceProtocol speed:(NSNumber *) speed productIDArray:(NSArray *) productIDArray;
```

#### Return Value

A dictionary to pass to IOKit matching methods, such as [`IOServiceGetMatchingService(_:_:)`](../../iokit/api-1514535-ioservicegetmatchingservice.md). The caller must release this object when done.

#### Discussion

The table below shows the keys you can use to make a successful matching dictionary. A plus sign (+) separates the keys to emphasize the requirement that all of the specified keys combine.

The table presents the keys in order of specificity. The first key defines the most specific search, and the last key defines the broadest search.

| Keys | Notes |
| --- | --- |
| [`idVendor`](../../iokit/iousbdevicedescriptor/api-1425819-idvendor.md) + [`idProduct`](../../iokit/iousbdevicedescriptor/api-1426145-idproduct.md) + [`bcdDevice`](../../iokit/iousbdevicedescriptor/api-1425514-bcddevice.md) | None. |
| [`idVendor`](../../iokit/iousbdevicedescriptor/api-1425819-idvendor.md) + [`idProduct`](../../iokit/iousbdevicedescriptor/api-1426145-idproduct.md) | None. |
| [`idVendor`](../../iokit/iousbdevicedescriptor/api-1425819-idvendor.md) + [`bDeviceSubClass`](../../iokit/iousbdevicedescriptor/api-1425757-bdevicesubclass.md) + [`bDeviceProtocol`](../../iokit/iousbdevicedescriptor/api-1425787-bdeviceprotocol.md) | Use these keys only if the device’s [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) is set to 0xFF. |
| [`idVendor`](../../iokit/iousbdevicedescriptor/api-1425819-idvendor.md) + [`bDeviceSubClass`](../../iokit/iousbdevicedescriptor/api-1425757-bdevicesubclass.md) | Use these keys only if the device’s [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) is set to 0xFF. |
| [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) + [`bDeviceSubClass`](../../iokit/iousbdevicedescriptor/api-1425757-bdevicesubclass.md) + [`bDeviceProtocol`](../../iokit/iousbdevicedescriptor/api-1425787-bdeviceprotocol.md) | Use these keys only if the device’s [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) is not set to 0xFF. |
| [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) + [`bDeviceSubClass`](../../iokit/iousbdevicedescriptor/api-1425757-bdevicesubclass.md) | Use these keys only if the device’s [`bDeviceClass`](../../iokit/iousbdevicedescriptor/api-1425902-bdeviceclass.md) is not set to 0xFF. |

## Parameters

- `vendorID`: The vendor ID for the device you’re searching for.
- `productID`: The product ID for the device you’re searching for.
- `bcdDevice`: The release number of the device you’re searching for.
- `deviceClass`: The class of the device you’re searching for.
- `deviceSubclass`: The subclass of the device you’re searching for.
- `deviceProtocol`: The protocol of the device you’re searching for.
- `speed`: The enumeration speed of the device you’re searching for. Add the speed to any of the keys in the table below.
- `productIDArray`: An array of product IDs to match against. Don’t use this parameter with the `productID` parameter.

## Topics

### Properties
- [struct IOUSBHostMatchingPropertyKey](../iousbhostmatchingpropertykey.md)
  Properties for implementing the matching service.
- [typealias IOUSBHostPropertyKey](../iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.

## See Also

### Related Documentation
- [class IOUSBHostDevice](../iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.
- [IOUSBDeviceDescriptor](../../iokit/iousbdevicedescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/creatematchingdictionarywithvendorid:productid:bcddevice:deviceclass:devicesubclass:deviceprotocol:speed:productidarray:)*