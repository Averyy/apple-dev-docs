# SACrashDetectionEvent

**Framework**: SafetyKit  
**Kind**: class

Describes the information about a vehicular crash.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
class SACrashDetectionEvent
```

#### Overview

When a vehicular crash occurs, SafetyKit calls your delegate’s [`crashDetectionManager(_:didDetect:)`](sacrashdetectiondelegate/crashdetectionmanager(_:diddetect:).md) method with an [`SACrashDetectionEvent`](sacrashdetectionevent.md) object. Inspect this object to determine information about the crash, including the date and time, location, and if the system attempted to contact emergency services.

## Topics

### Determining the event type
- [SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
- [var date: Date](sacrashdetectionevent/date.md)
  The date and time the crash occurred.
- [var location: CLLocation?](sacrashdetectionevent/location.md)
  The longitude and latitude where the crash detection occurred.
- [var response: SACrashDetectionEvent.Response](sacrashdetectionevent/response-swift.property.md)
  An indication of whether the system attempted to call an Emergency SOS provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SACrashDetectionManager](sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [enum SAAuthorizationStatus](saauthorizationstatus.md)
  An enumeration that represents the current Crash Detection event authorization state.
- [protocol SACrashDetectionDelegate](sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent)*