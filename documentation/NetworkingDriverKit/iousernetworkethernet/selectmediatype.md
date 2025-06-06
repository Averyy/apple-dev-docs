# SelectMediaType

**Framework**: NetworkingDriverKit  
**Kind**: method

Selects the media type to use when communicating with the network stack.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t SelectMediaType(IOUserNetworkMediaType mediaType);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Override this method and use it to configure your driver for the specified media type. In your implementation, validate the requested media type and make any adjustments as needed. For example, if the `mediaType` parameter is [`kIOUserNetworkMediaEthernetAuto`](kiousernetworkmediaethernetauto.md), you might choose an explicit media type instead. After validating the type, configure your driver for that type and call the [`ReportLinkStatus`](iousernetworkethernet/reportlinkstatus-5cxiq.md) method to report the driver’s status back to the system.

## Parameters

- `mediaType`: The media type to use for network communication. This type must be one that you declared previous when calling the   method.

## See Also

- [ReportAvailableMediaTypes](iousernetworkethernet/reportavailablemediatypes.md)
  Tells the system what types of networking media your driver supports.
- [IOUserNetworkMediaType](iousernetworkmediatype.md)
  A structure describing a specific Ethernet type and configuration that your driver supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/selectmediatype)*