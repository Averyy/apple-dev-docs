# home(_:didUpdateNameFor:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a home updated the name of a service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didUpdateNameFor group: HMServiceGroup)
```

```objc
- (void) home:(HMHome *) home didUpdateNameForServiceGroup:(HMServiceGroup *) group;
```

## Parameters

- `home`: The home.
- `group`: The service group whose name changed.

## See Also

### Observing Service Configuration
- [func home(HMHome, didAdd: HMServiceGroup)](./home%28_,didadd%29-3dymz.md)
  Tells the delegate that a home added a service group.
- [func home(HMHome, didAdd: HMService, to: HMServiceGroup)](./home%28_,didadd,to%29-6xdgy.md)
  Tells the delegate that a home added a service to a service group.
- [func home(HMHome, didRemove: HMService, from: HMServiceGroup)](./home%28_,didremove,from%29-9yzp0.md)
  Tells the delegate that a home removed a service from a service group.
- [func home(HMHome, didRemove: HMServiceGroup)](./home%28_,didremove%29-6kqxo.md)
  Tells the delegate that a home removed a service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didupdatenamefor:)-4tam1)*