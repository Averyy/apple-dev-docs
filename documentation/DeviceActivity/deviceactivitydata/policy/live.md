# DeviceActivityData.Policy.live

**Framework**: Device Activity  
**Kind**: case  
**Role**: Case

A policy that fetches live device activity data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case live
```

## Discussion

> **Note**:  A request to fetch live data may return cached data if the system updated the cache recently.

## See Also

### Fetching policies
- [DeviceActivityData.Policy.cached](./cached.md)
  A policy that fetches device activity data from the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/policy/live)*