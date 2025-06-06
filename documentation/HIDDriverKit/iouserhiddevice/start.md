# Start

**Framework**: HIDDriverKit  
**Kind**: method

Starts the device service and associates it with the specified provider object.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t Start(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

After successfully matching the specified provider to your device, the system instantiates your device object and calls this method. Don’t override this method directly. Instead, implement your custom initialization code in the [`handleStart`](iouserhiddevice/handlestart.md) method.

This method calls [`newDeviceDescription`](iouserhiddevice/newdevicedescription.md) and [`newReportDescriptor`](iouserhiddevice/newreportdescriptor.md) to retrieve information about your device. It then stores the results and starts your service.

## Parameters

- `provider`: The provider object that matches the current device. Cast this object to the class you expect. The system retains this object for the duration of your   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [handleStart](iouserhiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/start)*