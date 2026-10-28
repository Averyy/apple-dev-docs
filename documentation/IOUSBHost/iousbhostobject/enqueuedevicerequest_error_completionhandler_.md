# enqueueDeviceRequest:error:completionHandler:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enqueues a request on the default control endpoint without a data phase and a default timeout.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) enqueueDeviceRequest:(IOUSBDeviceRequest) request error:(NSError **) error completionHandler:(IOUSBHostCompletionHandler) completionHandler;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Discussion

This method enqueues an asynchronous request on the default control endpoint. If successful, `completionHandler` executes to report the status of the completed input/output request. This method uses `IOUSBHostDefaultControlCompletionTimeout` for the completion timeout.

## Parameters

- `request`: The device request to send.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.
- `completionHandler`: An [`IOUSBHostCompletionHandler`](../iousbhostcompletionhandler.md) that runs when the request completes or times out. The `completionHandler` doesn’t run if the method returns with an error.

## See Also

### Enqueueing Device Requests
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [- enqueueDeviceRequest:data:completionTimeout:error:completionHandler:](./enqueuedevicerequest_data_completiontimeout_error_completionhandler_.md)
  Enqueues a request on the default control endpoint.
- [- enqueueDeviceRequest:data:error:completionHandler:](./enqueuedevicerequest_data_error_completionhandler_.md)
  Enqueues a request on the default control endpoint with a default completion timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/enqueuedevicerequest:error:completionhandler:)*