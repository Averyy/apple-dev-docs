# sendDeviceRequest:data:bytesTransferred:completionTimeout:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Sends a request on the default control endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) sendDeviceRequest:(IOUSBDeviceRequest) request data:(NSMutableData *) data bytesTransferred:(NSUInteger *) bytesTransferred completionTimeout:(NSTimeInterval) completionTimeout error:(NSError **) error;
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

#### Discussion

This method sends a synchronous request on the default control endpoint, and doesn’t return until the request completes or times out.

## Parameters

- `request`: The device request to send.
- `data`: An [`NSMutableData`](../../Foundation/nsmutabledata.md) object defining the memory to use for the request’s data phase. The default is `nil`, meaning there’s no data phase for the control transfer.
- `bytesTransferred`: An [`NSUInteger`](../../ObjectiveC/nsuinteger.md) reference that updates with the byte count of the completed data phase.
- `completionTimeout`: A time interval representing the timeout of the request. If `0`, the request never times out. The default value is [`IOUSBHostDefaultControlCompletionTimeout`](../iousbhostdefaultcontrolcompletiontimeout.md).
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Sending Device Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](../iousbhostdevicerequesttype%28_,_,_%29.md)
  Creates the request type field of a device request.
- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](../iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.
- [- sendDeviceRequest:data:bytesTransferred:error:](./senddevicerequest_data_bytestransferred_error_.md)
  Sends a request on the default control endpoint with a default completion timeout.
- [- sendDeviceRequest:error:](./senddevicerequest_error_.md)
  Sends a request on the default control endpoint without a data phase and default completion timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/senddevicerequest:data:bytestransferred:completiontimeout:error:)*