# abortDeviceRequestsWithOption:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Aborts device requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) abortDeviceRequestsWithOption:(IOUSBHostAbortOption) option error:(NSError **) error;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Discussion

This method aborts any requests made with the [`sendDeviceRequest:data:bytesTransferred:completionTimeout:error:`](./senddevicerequest_data_bytestransferred_completiontimeout_error_.md) or [`enqueueDeviceRequest:data:completionTimeout:error:completionHandler:`](./enqueuedevicerequest_data_completiontimeout_error_completionhandler_.md) methods.

## Parameters

- `option`: A host abort option. The default value is [`IOUSBHostAbortOption.synchronous`](../iousbhostabortoption/synchronous.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## Topics

### Options
- [enum IOUSBHostAbortOption](../iousbhostabortoption.md)
  Options for aborting pending input/output requests.

## See Also

### Aborting Device Requests
- [enum IOUSBHostAbortOption](../iousbhostabortoption.md)
  Options for aborting pending input/output requests.
- [- abortDeviceRequestsWithError:](./abortdevicerequestswitherror_.md)
  Aborts device requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/abortdevicerequestswithoption:error:)*