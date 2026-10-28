# appCategory

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

An application category associated with this network slice.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
let appCategory: CTSlicingManager.AppCategory
```

## Discussion

This property identifies which type of application traffic the slice optimizes for, such as gaming, communication, or streaming.

## See Also

### Representing slice properties
- [let trafficClass: CTSlicingManager.TrafficClass?](./trafficclass.md)
  A traffic class that routes traffic through this network slice.
- [let networkInterfaceName: String](./networkinterfacename.md)
  A network interface name associated with the slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/slice/appcategory)*