# Start

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Starts the device service and associates it with the specified provider object.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t Start(IOService *provider);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

After successfully matching the specified provider to your device, the system instantiates your device object and calls this method. Don’t override this method directly. Instead, implement your custom initialization code in the [`handleStart`](./handlestart.md) method.

This method calls [`newDeviceDescription`](./newdevicedescription.md) and [`newReportDescriptor`](./newreportdescriptor.md) to retrieve information about your device. It then stores the results and starts your service.

## Parameters

- `provider`: The provider object that matches the current device. Cast this object to the class you expect. The system retains this object for the duration of your `Start` method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s [`Stop`](../iouserhideventservice/stop.md) method.

## See Also

### Running the Service
- [handleStart](./handlestart.md)
  Performs any custom initialization associated with starting the device service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/start)*