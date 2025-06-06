# homeManager(_:didAdd:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that the home manager added a home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func homeManager(_ manager: HMHomeManager, didAdd home: HMHome)
```

## Parameters

- `manager`: The home manager that added the home.
- `home`: The newly added home.

## See Also

- [func homeManagerDidUpdateHomes(HMHomeManager)](hmhomemanagerdelegate/homemanagerdidupdatehomes(_:).md)
  Tells the delegate that the home manager updated its collection of homes.
- [func homeManager(HMHomeManager, didRemove: HMHome)](hmhomemanagerdelegate/homemanager(_:didremove:).md)
  Tells the delegate that the home manager removed a home.
- [func homeManagerDidUpdatePrimaryHome(HMHomeManager)](hmhomemanagerdelegate/homemanagerdidupdateprimaryhome(_:).md)
  Tells the delegate that the home manager updated its primary home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanager(_:didadd:))*