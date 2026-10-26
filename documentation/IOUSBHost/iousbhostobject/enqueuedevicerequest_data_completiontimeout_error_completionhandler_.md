# enqueueDeviceRequest:data:completionTimeout:error:completionHandler:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Enqueues a request on the default control endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) enqueueDeviceRequest:(IOUSBDeviceRequest) request data:(NSMutableData *) data completionTimeout:(NSTimeInterval) completionTimeout error:(NSError **) error completionHandler:(IOUSBHostCompletionHandler) completionHandler;
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

#### Discussion

This method enqueues an asynchronous request on the default control endpoint. If successful, `completionHandler` executes to report the status of the completed input/output request.

## Parameters

- `request`: The device request to send.
- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the request’s data phase. The default is `nil`, meaning there’s no data phase for the control transfer.
- `completionTimeout`: A time interval representing the timeout of the request. If `0`, the request never times out. The default value is [`IOUSBHostDefaultControlCompletionTimeout`](../iousbhostdefaultcontrolcompletiontimeout.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.
- `completionHandler`: An [`IOUSBHostCompletionHandler`](../iousbhostcompletionhandler.md) that runs when the request completes or times out. The `completionHandler` doesn’t run if the method returns with an error.

## See Also

### Enqueueing Device Requests
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [- enqueueDeviceRequest:data:error:completionHandler:](./enqueuedevicerequest_data_error_completionhandler_.md)
  Enqueues a request on the default control endpoint with a default completion timeout.
- [- enqueueDeviceRequest:error:completionHandler:](./enqueuedevicerequest_error_completionhandler_.md)
  Enqueues a request on the default control endpoint without a data phase and a default timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/enqueuedevicerequest:data:completiontimeout:error:completionhandler:)*