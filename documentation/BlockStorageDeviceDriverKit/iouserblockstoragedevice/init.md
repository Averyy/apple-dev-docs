# init

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Handles the basic initialization of the service.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool init();
```

#### Return Value

Returns `true` if initialization was successful, or `false` if an error occurred.

#### Discussion

The system calls this method shortly after it instantiates your custom `IOUserBlockStorageDevice` subclass, and before it calls the [`Start`](iouserblockstoragedevice/start.md) method of your service. Limit the work you do in this method to simple tasks that must occur before your service starts. For example, use this method to allocate memory for your `ivars` structure.

Always call `super` early in your implementation of this method.

## See Also

- [Start](iouserblockstoragedevice/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserblockstoragedevice/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserblockstoragedevice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/init)*