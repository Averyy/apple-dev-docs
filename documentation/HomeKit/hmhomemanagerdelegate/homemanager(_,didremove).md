# homeManager(_:didRemove:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the home manager removed a home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func homeManager(_ manager: HMHomeManager, didRemove home: HMHome)
```

```objc
- (void) homeManager:(HMHomeManager *) manager didRemoveHome:(HMHome *) home;
```

## Parameters

- `manager`: The home manager that removed the home.
- `home`: The removed home.

## See Also

### Adding and removing homes
- [func homeManagerDidUpdateHomes(HMHomeManager)](./homemanagerdidupdatehomes%28_%29.md)
  Tells the delegate that the home manager updated its collection of homes.
- [func homeManager(HMHomeManager, didAdd: HMHome)](./homemanager%28_,didadd%29.md)
  Tells the delegate that the home manager added a home.
- [func homeManagerDidUpdatePrimaryHome(HMHomeManager)](./homemanagerdidupdateprimaryhome%28_%29.md)
  Tells the delegate that the home manager updated its primary home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanager(_:didremove:))*