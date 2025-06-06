# invalidateAuthorization(for:)

**Framework**: AVRouting  
**Kind**: method

Revokes an app’s authorization to connect to a route.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func invalidateAuthorization(for route: AVCustomDeviceRoute)
```

#### Discussion

The route only becomes authorized again if the user selects it using the route picker.

## Parameters

- `route`: The route to invalidate authorization for.

## See Also

- [var authorizedRoutes: [AVCustomDeviceRoute]](avcustomroutingcontroller/authorizedroutes.md)
  A list of authorized routes.
- [class let authorizedRoutesDidChange: NSNotification.Name](avcustomroutingcontroller/authorizedroutesdidchange.md)
  A notification the system posts when the list of authorized routes changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/invalidateauthorization(for:))*