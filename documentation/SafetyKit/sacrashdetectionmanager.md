# SACrashDetectionManager

**Framework**: SafetyKit  
**Kind**: class

Provides registration and management of Crash Detection events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
class SACrashDetectionManager
```

#### Overview

Use this class to determine Crash Detection availabilty on iPhone, detect authorization status, and register for Crash Detection events. Not all iPhones support Crash Detection, so verify that [`isAvailable`](sacrashdetectionmanager/isavailable.md) returns [`true`](https://developer.apple.com/documentation/Swift/true).

Check the value of [`authorizationStatus`](sacrashdetectionmanager/authorizationstatus.md) to determine if the person designates this app on their iPhone to receive Crash Detection events. If the value is not [`SAAuthorizationStatus.authorized`](saauthorizationstatus/authorized.md), set [`delegate`](sacrashdetectionmanager/delegate.md) and call [`requestAuthorization(completionHandler:)`](sacrashdetectionmanager/requestauthorization(completionhandler:).md) to request authorization.

After your app has authorization to receive Crash Detection events, adopt [`SACrashDetectionDelegate`](sacrashdetectiondelegate.md) and implement [`crashDetectionManager(_:didDetect:)`](sacrashdetectiondelegate/crashdetectionmanager(_:diddetect:).md). If a vehicular crash occurs, the system calls the method with the Crash Detection event.

## Topics

### Determining availability
- [class var isAvailable: Bool](sacrashdetectionmanager/isavailable.md)
  A Boolean value that indicates if Crash Detection is available.
- [var authorizationStatus: SAAuthorizationStatus](sacrashdetectionmanager/authorizationstatus.md)
  A value that indicates if the person authorized the app to receive Crash Detection events.
### Requesting authorization
- [var delegate: (any SACrashDetectionDelegate)?](sacrashdetectionmanager/delegate.md)
  The object that receives Crash Detection events.
- [func requestAuthorization(completionHandler: (SAAuthorizationStatus, (any Error)?) -> Void)](sacrashdetectionmanager/requestauthorization(completionhandler:).md)
  Requests permission to access Crash Detection information.

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

- [enum SAAuthorizationStatus](saauthorizationstatus.md)
  An enumeration that represents the current Crash Detection event authorization state.
- [class SACrashDetectionEvent](sacrashdetectionevent.md)
  Describes the information about a vehicular crash.
- [protocol SACrashDetectionDelegate](sacrashdetectiondelegate.md)
  The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager)*