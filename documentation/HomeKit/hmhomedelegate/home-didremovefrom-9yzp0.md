# home(_:didRemove:from:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a home removed a service from a service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didRemove service: HMService, from group: HMServiceGroup)
```

## Parameters

- `home`: The home.
- `service`: The service that was removed.
- `group`: The group from which the service was removed.

## See Also

- [func home(HMHome, didAdd: HMServiceGroup)](hmhomedelegate/home(_:didadd:)-3dymz.md)
  Tells the delegate that a home added a service group.
- [func home(HMHome, didUpdateNameFor: HMServiceGroup)](hmhomedelegate/home(_:didupdatenamefor:)-4tam1.md)
  Tells the delegate that a home updated the name of a service group.
- [func home(HMHome, didAdd: HMService, to: HMServiceGroup)](hmhomedelegate/home(_:didadd:to:)-6xdgy.md)
  Tells the delegate that a home added a service to a service group.
- [func home(HMHome, didRemove: HMServiceGroup)](hmhomedelegate/home(_:didremove:)-6kqxo.md)
  Tells the delegate that a home removed a service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didremove:from:)-9yzp0)*