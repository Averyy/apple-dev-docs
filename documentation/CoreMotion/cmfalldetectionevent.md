# CMFallDetectionEvent

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

An object that contains data about a fall detection event.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
class CMFallDetectionEvent
```

```objc
@interface CMFallDetectionEvent : NSObject
```

## Topics

### Accessing Fall Data
- [var resolution: CMFallDetectionEvent.UserResolution](./cmfalldetectionevent/resolution.md)
  The event’s resolution.
- [CMFallDetectionEvent.UserResolution](./cmfalldetectionevent/userresolution.md)
  User resolutions for fall detection events.
### Getting the event date
- [var date: Date](./cmfalldetectionevent/date.md)
  The event’s time and date.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Fall detection
- [class CMFallDetectionManager](./cmfalldetectionmanager.md)
  An object for managing fall detection events.
- [protocol CMFallDetectionDelegate](./cmfalldetectiondelegate.md)
  A delegate that receives information about fall detection events and authorization status changes.
- [NSFallDetectionUsageDescription](../BundleResources/information-property-list/nsfalldetectionusagedescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent)*