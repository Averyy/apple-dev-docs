# abortDeviceRequestsWithError:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Aborts device requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) abortDeviceRequestsWithError:(NSError **) error;
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

#### Discussion

This method aborts any requests made with the [`sendDeviceRequest:data:bytesTransferred:completionTimeout:error:`](./senddevicerequest_data_bytestransferred_completiontimeout_error_.md) or [`enqueueDeviceRequest:data:completionTimeout:error:completionHandler:`](./enqueuedevicerequest_data_completiontimeout_error_completionhandler_.md) methods.

## See Also

### Aborting Device Requests
- [enum IOUSBHostAbortOption](../iousbhostabortoption.md)
  Options for aborting pending input/output requests.
- [- abortDeviceRequestsWithOption:error:](./abortdevicerequestswithoption_error_.md)
  Aborts device requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/abortdevicerequestswitherror:)*