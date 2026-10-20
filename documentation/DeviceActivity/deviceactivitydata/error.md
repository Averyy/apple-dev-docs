# DeviceActivityData.Error

**Framework**: Device Activity  
**Kind**: enum  
**Role**: Enumeration

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
- [DeviceActivityData.Error.unavailable](./error/unavailable.md)
  An error indicating data access is unavailable.
- [DeviceActivityData.Error.unauthorized](./error/unauthorized.md)
  An error indicating the app isn’t authorized to provide parental controls and access data.
- [DeviceActivityData.Error.missingData](./error/missingdata.md)
  An error indicating the requested data does not exist.
### Describing errors
- [var errorDescription: String?](./error/errordescription.md)
  A localized message that describes what error occurred.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing data access
- [DeviceActivityData.Policy](./policy.md)
  The policy for fetching activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/error)*