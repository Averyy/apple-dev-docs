# CMTimebase.Error

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Constants that describe timebase errors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Error
```

## Topics

### Constants
- [static let allocationFailed: NSError](./error/allocationfailed.md)
  A timebase error that indicates the memory allocation fails.
- [static let invalidParameter: NSError](./error/invalidparameter.md)
  A timebase error that indicates a parameter isn’t valid.
- [static let missingRequiredParameter: NSError](./error/missingrequiredparameter.md)
  A timebase error that indicates a missing parameter.
- [static let readOnly: NSError](./error/readonly.md)
  A timebase error that indicates the system attempts to modify a read-only timebase.
- [static let timerIntervalTooShort: NSError](./error/timerintervaltooshort.md)
  A timebase error that indicates the time interval is too short.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [CMTimebase.NotificationKey](./notificationkey.md)
  Constants that describe notification keys.
- [static var typeID: CFTypeID](./typeid.md)
  A Core Foundation type identifier that represents a timebase object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/error)*