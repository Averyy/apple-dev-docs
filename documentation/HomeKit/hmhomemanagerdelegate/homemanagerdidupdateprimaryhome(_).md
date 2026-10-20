# homeManagerDidUpdatePrimaryHome(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the home manager updated its primary home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager)
```

```objc
- (void) homeManagerDidUpdatePrimaryHome:(HMHomeManager *) manager;
```

## Parameters

- `manager`: The home manager with an updated primary home.

## See Also

### Adding and removing homes
- [func homeManagerDidUpdateHomes(HMHomeManager)](./homemanagerdidupdatehomes%28_%29.md)
  Tells the delegate that the home manager updated its collection of homes.
- [func homeManager(HMHomeManager, didAdd: HMHome)](./homemanager%28_,didadd%29.md)
  Tells the delegate that the home manager added a home.
- [func homeManager(HMHomeManager, didRemove: HMHome)](./homemanager%28_,didremove%29.md)
  Tells the delegate that the home manager removed a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanagerdidupdateprimaryhome(_:))*