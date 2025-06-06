# ReportLinkStatus

**Framework**: NetworkingDriverKit  
**Kind**: method

Reports the status of the link between the device and your driver to the system.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t ReportLinkStatus(IOUserNetworkLinkStatus linkStatus, IOUserNetworkMediaType activeMediaType);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Call this method when you want to notify the network about any changes to the link status or active media type for your device.

## Parameters

- `linkStatus`: The state of the connection to your device. For a list of possible values, see the constants in  .
- `activeMediaType`: The media type that your device currently supports. The media type must be one you previously reported using the   method.

## See Also

- [ReportLinkQuality](iousernetworkethernet/reportlinkquality-4noh0.md)
  Reports the quality of the link between the device and your driver to the system.
- [ReportDataBandwidths](iousernetworkethernet/reportdatabandwidths-10ssx.md)
  Reports the input and output bandwidth between the device and your driver to the system.
- [IOUserNetworkLinkStatus](iousernetworklinkstatus.md)
  A type for specifying the state of your device’s connection.
- [IOUserNetworkLinkQuality](iousernetworklinkquality.md)
  A type for specifying the quality of your device’s connection to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/reportlinkstatus-5cxiq)*