# setActive(_:for:)

**Framework**: AVRouting  
**Kind**: method

Sets the active state of a route.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func setActive(_ active: Bool, for route: AVCustomDeviceRoute)
```

#### Discussion

Set the value to [`false`](https://developer.apple.com/documentation/Swift/false) if the connection to the route becomes unavailable, and set it to [`true`](https://developer.apple.com/documentation/Swift/true) after you reestablish the connection.

## Parameters

- `active`: A Boolean value that indicates whether the route is active.
- `route`: A route to change the active state for.

## See Also

- [func isRouteActive(AVCustomDeviceRoute) -> Bool](avcustomroutingcontroller/isrouteactive(_:).md)
  Returns a Boolean value that indicates whether a route is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/setactive(_:for:))*