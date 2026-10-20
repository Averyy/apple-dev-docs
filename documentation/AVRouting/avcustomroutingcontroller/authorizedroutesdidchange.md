# authorizedRoutesDidChange

**Framework**: AVRouting  
**Kind**: property  
**Role**: Type Property

A notification the system posts when the list of authorized routes changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class let authorizedRoutesDidChange: NSNotification.Name
```

```c
extern NSNotificationName const AVCustomRoutingControllerAuthorizedRoutesDidChangeNotification;
```

## See Also

### Managing authorization
- [var authorizedRoutes: [AVCustomDeviceRoute]](./authorizedroutes.md)
  A list of authorized routes.
- [func invalidateAuthorization(for: AVCustomDeviceRoute)](./invalidateauthorization%28for%29.md)
  Revokes an app’s authorization to connect to a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/authorizedroutesdidchange)*