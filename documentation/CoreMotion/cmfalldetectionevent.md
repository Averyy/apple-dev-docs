# CMFallDetectionEvent

**Framework**: Core Motion  
**Kind**: class

An object that contains data about a fall detection event.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
class CMFallDetectionEvent
```

## Topics

### Accessing Fall Data
- [var resolution: CMFallDetectionEvent.UserResolution](cmfalldetectionevent/resolution.md)
  The event’s resolution.
- [CMFallDetectionEvent.UserResolution](cmfalldetectionevent/userresolution.md)
  User resolutions for fall detection events.
### Getting the event date
- [var date: Date](cmfalldetectionevent/date.md)
  The event’s time and date.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMFallDetectionManager](cmfalldetectionmanager.md)
  An object for managing fall detection events.
- [protocol CMFallDetectionDelegate](cmfalldetectiondelegate.md)
  A delegate that receives information about fall detection events and authorization status changes.
- [NSFallDetectionUsageDescription](../BundleResources/Information-Property-List/NSFallDetectionUsageDescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)*