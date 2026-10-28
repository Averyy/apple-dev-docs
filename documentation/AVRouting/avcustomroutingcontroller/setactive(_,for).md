# setActive(_:for:)

**Framework**: AVRouting  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setActive:(BOOL) active forRoute:(AVCustomDeviceRoute *) route;
```

## Discussion

Set the value to [`false`](../../Swift/false.md) if the connection to the route becomes unavailable, and set it to [`true`](../../Swift/true.md) after you reestablish the connection.

## Parameters

- `active`: A Boolean value that indicates whether the route is active.
- `route`: A route to change the active state for.

## See Also

### Activating a route
- [func isRouteActive(AVCustomDeviceRoute) -> Bool](./isrouteactive%28_%29.md)
  Returns a Boolean value that indicates whether a route is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/setactive(_:for:))*