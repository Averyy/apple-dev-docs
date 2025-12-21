# isRouteActive(_:)

**Framework**: AVRouting  
**Kind**: method

Returns a Boolean value that indicates whether a route is active.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func isRouteActive(_ route: AVCustomDeviceRoute) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the route is in an active state; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `route`: A route for determining its active state.

## See Also

- [func setActive(Bool, for: AVCustomDeviceRoute)](avcustomroutingcontroller/setactive(_:for:).md)
  Sets the active state of a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/isrouteactive(_:))*