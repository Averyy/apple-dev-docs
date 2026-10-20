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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdefaultcontrolcompletiontimeout)*