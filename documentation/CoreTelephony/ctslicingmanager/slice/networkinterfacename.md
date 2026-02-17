# networkInterfaceName

**Framework**: Core Telephony  
**Kind**: property

A network interface name associated with the slice.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
let networkInterfaceName: String
```

#### Discussion

This property contains the system name of the network interface that handles traffic for this network slice, such as “pdp_ip0”.

## See Also

- [let appCategory: CTSlicingManager.AppCategory](ctslicingmanager/slice/appcategory.md)
  An application category associated with this network slice.
- [let trafficClass: CTSlicingManager.TrafficClass?](ctslicingmanager/slice/trafficclass.md)
  A traffic class that routes traffic through this network slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/slice/networkinterfacename)*