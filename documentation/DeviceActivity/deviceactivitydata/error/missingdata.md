# DeviceActivityData.Error.missingData

**Framework**: Device Activity  
**Kind**: case

An error indicating the requested data does not exist.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
case missingData
```

#### Discussion

If fetching cached data returns this error, fetching live data may resolve the issue.

## See Also

- [DeviceActivityData.Error.unavailable](deviceactivitydata/error/unavailable.md)
  An error indicating data access is unavailable.
- [DeviceActivityData.Error.unauthorized](deviceactivitydata/error/unauthorized.md)
  An error indicating the app isn’t authorized to provide parental controls and access data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/error/missingdata)*