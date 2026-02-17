# appCategory

**Framework**: Core Telephony  
**Kind**: property

An application category associated with this network slice.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
let appCategory: CTSlicingManager.AppCategory
```

#### Discussion

This property identifies which type of application traffic the slice optimizes for, such as gaming, communication, or streaming.

## See Also

- [let trafficClass: CTSlicingManager.TrafficClass?](ctslicingmanager/slice/trafficclass.md)
  A traffic class that routes traffic through this network slice.
- [let networkInterfaceName: String](ctslicingmanager/slice/networkinterfacename.md)
  A network interface name associated with the slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/slice/appcategory)*