# DeviceActivityData.Error

**Framework**: Device Activity  
**Kind**: enum

Errors that may occur when attempting to fetch activity data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum Error
```

## Topics

### Representing errors
- [DeviceActivityData.Error.unavailable](deviceactivitydata/error/unavailable.md)
  An error indicating data access is unavailable.
- [DeviceActivityData.Error.unauthorized](deviceactivitydata/error/unauthorized.md)
  An error indicating the app isn’t authorized to provide parental controls and access data.
- [DeviceActivityData.Error.missingData](deviceactivitydata/error/missingdata.md)
  An error indicating the requested data does not exist.
### Describing errors
- [var errorDescription: String?](deviceactivitydata/error/errordescription.md)
  A localized message that describes what error occurred.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DeviceActivityData.Policy](deviceactivitydata/policy.md)
  The policy for fetching activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/error)*