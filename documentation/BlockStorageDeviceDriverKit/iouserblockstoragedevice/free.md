# free

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual void free();
```

## Discussion

Use this method to perform tasks such as deallocating any allocated memory. The system calls this method at some point after it calls your service’s [`Stop`](./stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

### Running the Service
- [init](./init.md)
  Handles the basic initialization of the service.
- [Start](./start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](./stop.md)
  Stops the service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/free)*