# IOUSBHostDefaultControlCompletionTimeout

**Framework**: IOUSBHost  
**Kind**: var  
**Role**: Global Variable

The default completion timeout for input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
let IOUSBHostDefaultControlCompletionTimeout: TimeInterval
```

```c
extern const NSTimeInterval IOUSBHostDefaultControlCompletionTimeout;
```

## See Also

### Sending Device Requests
- [func IOUSBHostDeviceRequestType(tIOUSBDeviceRequestDirectionValue, tIOUSBDeviceRequestTypeValue, tIOUSBDeviceRequestRecipientValue) -> UInt8](./iousbhostdevicerequesttype%28_,_,_%29.md)
  Creates the request type field of a device request.
- [- sendDeviceRequest:data:bytesTransferred:completionTimeout:error:](./iousbhostobject/senddevicerequest_data_bytestransferred_completiontimeout_error_.md)
  Sends a request on the default control endpoint.
- [- sendDeviceRequest:data:bytesTransferred:error:](./iousbhostobject/senddevicerequest_data_bytestransferred_error_.md)
  Sends a request on the default control endpoint with a default completion timeout.
- [- sendDeviceRequest:error:](./iousbhostobject/senddevicerequest_error_.md)
  Sends a request on the default control endpoint without a data phase and default completion timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdefaultcontrolcompletiontimeout)*