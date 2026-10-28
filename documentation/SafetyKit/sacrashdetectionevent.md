# SACrashDetectionEvent

**Framework**: SafetyKit  
**Kind**: class  
**Role**: Class

Describes the information about a vehicular crash.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
class SACrashDetectionEvent
```

```objc
@interface SACrashDetectionEvent : NSObject
```

## Overview

When a vehicular crash occurs, SafetyKit calls your delegate’s [`crashDetectionManager(_:didDetect:)`](./sacrashdetectiondelegate/crashdetectionmanager%28_,diddetect%29.md) method with an [`SACrashDetectionEvent`](./sacrashdetectionevent.md) object. Inspect this object to determine information about the crash, including the date and time, location, and if the system attempted to contact emergency services.

## Topics

### Determining the event type
- [SACrashDetectionEvent.Response](./sacrashdetectionevent/response-swift.enum.md)
  An enumeration that defines possible emergency responses to a Crash Detection event.
- [var date: Date](./sacrashdetectionevent/date.md)
  The date and time the crash occurred.
- [var location: CLLocation?](./sacrashdetectionevent/location.md)
  The longitude and latitude where the crash detection occurred.
- [var response: SACrashDetectionEvent.Response](./sacrashdetectionevent/response-swift.property.md)
  An indication of whether the system attempted to call an Emergency SOS provider.
### Initializers
- [init?(coder: NSCoder)](./sacrashdetectionevent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Detecting a crash
- [class SACrashDetectionManager](./sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [enum SAAuthorizationStatus](./saauthorizationstatus.md)
  An enumeration that represents the current Crash Detection event authorization state.
- [protocol SACrashDetectionDelegate](./sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent)*