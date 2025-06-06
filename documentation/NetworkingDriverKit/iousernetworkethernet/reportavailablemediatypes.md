# ReportAvailableMediaTypes

**Framework**: NetworkingDriverKit  
**Kind**: method

Tells the system what types of networking media your driver supports.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t ReportAvailableMediaTypes(const IOUserNetworkMediaType * mediaTypes, uint32_t count);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Apple recommends that you include [`kIOUserNetworkMediaEthernetAuto`](kiousernetworkmediaethernetauto.md) as one of the media types you support. That media type lets the system configure the networking stack automatically on your behalf, based on the other media types you specify.

## Parameters

- `mediaTypes`: An array of   types. For each type, combine a   constant with one or more   constants to indicate the configurations you support.
- `count`: The number of items in the   array.

## See Also

- [SelectMediaType](iousernetworkethernet/selectmediatype.md)
  Selects the media type to use when communicating with the network stack.
- [IOUserNetworkMediaType](iousernetworkmediatype.md)
  A structure describing a specific Ethernet type and configuration that your driver supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/reportavailablemediatypes)*