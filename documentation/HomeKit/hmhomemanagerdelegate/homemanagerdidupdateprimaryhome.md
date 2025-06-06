# homeManagerDidUpdatePrimaryHome(_:)

**Framework**: HomeKit  
**Kind**: method

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

## Parameters

- `manager`: The home manager with an updated primary home.

## See Also

- [func homeManagerDidUpdateHomes(HMHomeManager)](hmhomemanagerdelegate/homemanagerdidupdatehomes(_:).md)
  Tells the delegate that the home manager updated its collection of homes.
- [func homeManager(HMHomeManager, didAdd: HMHome)](hmhomemanagerdelegate/homemanager(_:didadd:).md)
  Tells the delegate that the home manager added a home.
- [func homeManager(HMHomeManager, didRemove: HMHome)](hmhomemanagerdelegate/homemanager(_:didremove:).md)
  Tells the delegate that the home manager removed a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanagerdidupdateprimaryhome(_:))*