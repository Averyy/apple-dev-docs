# dispatchSetReportRequest(type:id:data:timeout:)

**Framework**: Core HID  
**Kind**: method  
**Role**: Instance Method

Send a set report request to the device over the transport.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func dispatchSetReportRequest(type: HIDReportType, id: HIDReportID? = nil, data: Data, timeout: Duration? = nil) async throws
```

## Mentions

- [Creating virtual devices](../creatingvirtualdevices.md)

#### Discussion

Many HID devices accept set report requests to send data to the device or alter functionality. Exactly how a device interprets a set report depends on the device specific implementation, but most devices conform to the reports that they declare in their report [`descriptor`](./descriptor.md). This function throws if another client obtains the device.

For more details, see [Human Interface Devices (HID) Specifications and Tools](https://www.usb.org/hid).

> **Throws**: [`HIDDeviceError`](../hiddeviceerror.md) if there is an issue with the request.

## Parameters

- `type`: The [`HIDReportType`](../hidreporttype.md) of the report.
- `id`: The ID of the provided report, determined from the report descriptor. This is unnecessary if the descriptor has only one report.
- `data`: The bytes to send as a part of the request. Determining the correct values can be aided by referencing the device’s [`descriptor`](./descriptor.md).
- `timeout`: The maximum amount of time to wait for the device to receive the report before the calls time out and fails. Not providing a duration causes the call to wait forever.

## See Also

### Interact with the device
- [func dispatchGetReportRequest(type: HIDReportType, id: HIDReportID?, timeout: Duration?) async throws -> Data](./dispatchgetreportrequest%28type,id,timeout%29.md)
  Send a get report request to the device over the transport.
- [func seizeDevice() throws](./seizedevice%28%29.md)
  Attempt to obtain the device so that this client is the only active client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/dispatchsetreportrequest(type:id:data:timeout:))*