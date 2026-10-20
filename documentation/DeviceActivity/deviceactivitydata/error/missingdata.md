# DeviceActivityData.Error.missingData

**Framework**: Device Activity  
**Kind**: case  
**Role**: Case

An error indicating the requested data does not exist.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case missingData
```

#### Discussion

If fetching cached data returns this error, fetching live data may resolve the issue.

## See Also

### Representing errors
- [DeviceActivityData.Error.unavailable](./unavailable.md)
  An error indicating data access is unavailable.
- [DeviceActivityData.Error.unauthorized](./unauthorized.md)
  An error indicating the app isn’t authorized to provide parental controls and access data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/error/missingdata)*