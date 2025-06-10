# AppExtensionPoint.Monitor

**Framework**: ExtensionFoundation  
**Kind**: class

An object that monitors the app extension points you add to it

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
final class Monitor
```

## Topics

### Structures
- [AppExtensionPoint.Monitor.State](appextensionpoint/monitor/state-swift.struct.md)
  The snapshot of the current Monitor state
### Initializers
- [init()](appextensionpoint/monitor/init.md)
  Creates an app extesion point monitor
- [convenience init(appExtensionPoint: AppExtensionPoint) async throws](appextensionpoint/monitor/init(appextensionpoint:).md)
  Creates an app extesion point monitor and starts monitoring the given app extension point
### Instance Properties
- [var identities: [AppExtensionIdentity]](appextensionpoint/monitor/identities.md)
  An array of `AppExtensionIdentity` objects representing available app extensions bound to the monitored app extension points.
- [var state: AppExtensionPoint.Monitor.State](appextensionpoint/monitor/state-swift.property.md)
  An observable monitor state
### Instance Methods
- [func addAppExtensionPoint(AppExtensionPoint) async throws](appextensionpoint/monitor/addappextensionpoint(_:).md)
  Adds the given app extension point to the monitor
- [func removeAppExtensionPoint(AppExtensionPoint) async throws](appextensionpoint/monitor/removeappextensionpoint(_:).md)
  Removes the app extension point from the monitor

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor)*