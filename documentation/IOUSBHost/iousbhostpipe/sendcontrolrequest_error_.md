# sendControlRequest:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Sends a request on a control endpoint without a data phase and a default completion timeout.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) sendControlRequest:(IOUSBDeviceRequest) request error:(NSError **) error;
```

## Return Value

`YES` if the abort completes successfully; otherwise, `NO`.

## Discussion

This method sends a synchronous request on the default control endpoint, and doesn’t return until the request is complete or times out. This method uses [`IOUSBHostDefaultControlCompletionTimeout`](../iousbhostdefaultcontrolcompletiontimeout.md) at the input/output request’s `completionTimeout`.

## Parameters

- `request`: The device request to send.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Sending Control Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](../iousbhostdevicerequesttype%28_,_,_%29.md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](../iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [typealias IOUSBHostCompletionHandler](../iousbhostcompletionhandler.md)
  The completion handler for asynchronous control, bulk, and interrupt transfers.
- [- enqueueControlRequest:data:completionTimeout:error:completionHandler:](./enqueuecontrolrequest_data_completiontimeout_error_completionhandler_.md)
  Enqueues a request on a control endpoint.
- [- enqueueControlRequest:data:error:completionHandler:](./enqueuecontrolrequest_data_error_completionhandler_.md)
  Enqueues a request on a control endpoint with a default completion timeout.
- [- enqueueControlRequest:error:completionHandler:](./enqueuecontrolrequest_error_completionhandler_.md)
  Enqueues a request on a control endpoint without a data phase and a default completion timeout.
- [- sendControlRequest:data:bytesTransferred:completionTimeout:error:](./sendcontrolrequest_data_bytestransferred_completiontimeout_error_.md)
  Sends a request on a control endpoint.
- [- sendControlRequest:data:bytesTransferred:error:](./sendcontrolrequest_data_bytestransferred_error_.md)
  Sends a request on a control endpoint with a default timeout.
- [- abortWithOption:error:](./abortwithoption_error_.md)
  Aborts pending input/output requests.
- [- abortWithError:](./abortwitherror_.md)
  Aborts pending input/output requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendcontrolrequest:error:)*