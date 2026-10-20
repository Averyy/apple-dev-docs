# trafficClass

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A traffic class that routes traffic through this network slice.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
let trafficClass: CTSlicingManager.TrafficClass?
```

#### Discussion

The traffic class indicates the quality of service characteristics for the slice, such as voice, video, or background data. When the network slice doesn’t have a specific traffic class restriction, this property returns [`CTSlicingManager.TrafficClass.any`](../trafficclass/any.md), indicating the slice can handle all types of network traffic.

## See Also

### Representing slice properties
- [let appCategory: CTSlicingManager.AppCategory](./appcategory.md)
  An application category associated with this network slice.
- [let networkInterfaceName: String](./networkinterfacename.md)
  A network interface name associated with the slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/slice/trafficclass)*