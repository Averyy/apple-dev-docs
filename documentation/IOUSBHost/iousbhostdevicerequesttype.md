# IOUSBHostDeviceRequestType(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Creates the request type field of a device request.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBHostDeviceRequestType(_ direction: tIOUSBDeviceRequestDirectionValue, _ type: tIOUSBDeviceRequestTypeValue, _ recipient: tIOUSBDeviceRequestRecipientValue) -> UInt8
```

#### Return Value

The request type.

## Parameters

- `direction`: The direction of the request.
- `type`: The type of the request.
- `recipient`: The recipient of the request.

## See Also

- [let IOUSBHostDefaultControlCompletionTimeout: TimeInterval](iousbhostdefaultcontrolcompletiontimeout.md)
  The default completion timeout for input/output requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevicerequesttype(_:_:_:))*