# isRouteActive(_:)

**Framework**: AVRouting  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isRouteActive:(AVCustomDeviceRoute *) route;
```

## Return Value

[`true`](../../Swift/true.md) if the route is in an active state; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `route`: A route for determining its active state.

## See Also

### Activating a route
- [func setActive(Bool, for: AVCustomDeviceRoute)](./setactive%28_,for%29.md)
  Sets the active state of a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/isrouteactive(_:))*