# IOUSBHostCompletionHandler

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

The completion handler for asynchronous control, bulk, and interrupt transfers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostCompletionHandler = (IOReturn, Int) -> Void
```

```c
typedef void (^)(int, unsigned long) IOUSBHostCompletionHandler;
```

## Parameters

- `status`: The result for the transfer.
- `bytesTransferred`: The number of bytes the request transferred.

## See Also

### Enqueueing Device Requests
- [- enqueueDeviceRequest:data:completionTimeout:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_data_completiontimeout_error_completionhandler_.md)
  Enqueues a request on the default control endpoint.
- [- enqueueDeviceRequest:data:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_data_error_completionhandler_.md)
  Enqueues a request on the default control endpoint with a default completion timeout.
- [- enqueueDeviceRequest:error:completionHandler:](./iousbhostobject/enqueuedevicerequest_error_completionhandler_.md)
  Enqueues a request on the default control endpoint without a data phase and a default timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcompletionhandler)*