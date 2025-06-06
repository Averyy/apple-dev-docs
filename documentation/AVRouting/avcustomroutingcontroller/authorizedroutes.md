# authorizedRoutes

**Framework**: AVRouting  
**Kind**: property

A list of authorized routes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var authorizedRoutes: [AVCustomDeviceRoute] { get }
```

#### Discussion

After a user activates a route, it remains authorized for a certain amount of time even if the connection to the route is temporarily unavailable. Your app may reactivate any one of these routes when appropriate, but it needs to inform the system by calling [`setActive(_:for:)`](avcustomroutingcontroller/setactive(_:for:).md).

## See Also

- [class let authorizedRoutesDidChange: NSNotification.Name](avcustomroutingcontroller/authorizedroutesdidchange.md)
  A notification the system posts when the list of authorized routes changes.
- [func invalidateAuthorization(for: AVCustomDeviceRoute)](avcustomroutingcontroller/invalidateauthorization(for:).md)
  Revokes an app’s authorization to connect to a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/authorizedroutes)*