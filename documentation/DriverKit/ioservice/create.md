# Create

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Requests the creation of a new service object.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t Create(IOService *provider, const IOPropertyName propertiesKey, IOService **result);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../error-codes.md).

## Discussion

Call this method from your NewUserClient method when the system asks you to create a new service. The keys in the `propertiesKey` dictionary describe the new service. Use the [`kIOUserClassKey`](../../iokit/kiouserclasskey.md) key to specify the name of the custom [`IOService`](../ioservice.md) subclass that you want the system to instantiate. Use the [`kIOClassKey`](../../iokit/kioclasskey.md) to specify the name of the custom [`IOUserClient`](../iouserclient.md) subclass to return to clients of your service. Use the [`kIOServiceDEXTEntitlementsKey`](../../iokit/kioservicedextentitlementskey.md) key to specify an array of entitlement strings to match against the process of the new service. The new service must contain all of the requested entitlements.

## Parameters

- `provider`: The provider to associate with the new service object. Always specify the current service object as the provider.
- `propertiesKey`: The name of a property associated with the current service. The value of this property must be an [`OSDictionary`](../osdictionary.md) object, and the dictionary should contain the [`kIOClassKey`](../../iokit/kioclasskey.md), [`kIOUserClassKey`](../../iokit/kiouserclasskey.md), and [`kIOServiceDEXTEntitlementsKey`](../../iokit/kioservicedextentitlementskey.md) matching keys.
- `result`: The service object for the newly created service. The class of this object is the one you specified using the [`kIOClassKey`](../../iokit/kioclasskey.md) in the `propertiesKey` dictionary This method retains the object, and you are responsible for releasing it.

## See Also

### Creating a New Service
- [NewUserClient](./newuserclient.md)
  Requests the creation of a new user client for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/create)*