# home(_:didAdd:to:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a home added a service to a service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didAdd service: HMService, to group: HMServiceGroup)
```

```objc
- (void) home:(HMHome *) home didAddService:(HMService *) service toServiceGroup:(HMServiceGroup *) group;
```

## Parameters

- `home`: The home.
- `service`: The service that was added.
- `group`: The group to which the service was added.

## See Also

### Observing Service Configuration
- [func home(HMHome, didAdd: HMServiceGroup)](./home%28_,didadd%29-3dymz.md)
  Tells the delegate that a home added a service group.
- [func home(HMHome, didUpdateNameFor: HMServiceGroup)](./home%28_,didupdatenamefor%29-4tam1.md)
  Tells the delegate that a home updated the name of a service group.
- [func home(HMHome, didRemove: HMService, from: HMServiceGroup)](./home%28_,didremove,from%29-9yzp0.md)
  Tells the delegate that a home removed a service from a service group.
- [func home(HMHome, didRemove: HMServiceGroup)](./home%28_,didremove%29-6kqxo.md)
  Tells the delegate that a home removed a service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didadd:to:)-6xdgy)*