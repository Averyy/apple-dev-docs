# SACrashDetectionDelegate

**Framework**: SafetyKit  
**Kind**: protocol

The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
protocol SACrashDetectionDelegate : NSObjectProtocol
```

#### Overview

Upon app launch, immediately set the delegate so it receives Crash Detection events. If the app isn’t running, the system launches it in the background and then sends the event.

## Topics

### Obtaining a Crash Detection event
- [func crashDetectionManager(SACrashDetectionManager, didDetect: SACrashDetectionEvent)](sacrashdetectiondelegate/crashdetectionmanager(_:diddetect:).md)
  Receive and process a Crash Detection event.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SACrashDetectionManager](sacrashdetectionmanager.md)
  Provides registration and management of Crash Detection events.
- [enum SAAuthorizationStatus](saauthorizationstatus.md)
  An enumeration that represents the current Crash Detection event authorization state.
- [class SACrashDetectionEvent](sacrashdetectionevent.md)
  Describes the information about a vehicular crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectiondelegate)*