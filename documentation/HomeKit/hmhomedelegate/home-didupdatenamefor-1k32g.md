# home(_:didUpdateNameFor:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a home changed the name of a zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didUpdateNameFor zone: HMZone)
```

## Parameters

- `home`: The home.
- `zone`: The zone whose name was changed.

## See Also

- [func homeDidUpdateName(HMHome)](hmhomedelegate/homedidupdatename(_:).md)
  Tells the delegate that a home’s name changed.
- [func home(HMHome, didAdd: HMAccessory)](hmhomedelegate/home(_:didadd:)-6jcl7.md)
  Tells the delegate that a home added a new accessory.
- [func home(HMHome, didUpdate: HMRoom, for: HMAccessory)](hmhomedelegate/home(_:didupdate:for:).md)
  Tells the delegate that a home assigned an accessory to a different room.
- [func home(HMHome, didRemove: HMAccessory)](hmhomedelegate/home(_:didremove:)-6plye.md)
  Tells the delegate that a home removed an accessory.
- [func home(HMHome, didAdd: HMRoom)](hmhomedelegate/home(_:didadd:)-42aqd.md)
  Tells the delegate that a home added a new room.
- [func home(HMHome, didUpdateNameFor: HMRoom)](hmhomedelegate/home(_:didupdatenamefor:)-1a110.md)
  Tells the delegate that a home updated the name of one of its rooms.
- [func home(HMHome, didAdd: HMRoom, to: HMZone)](hmhomedelegate/home(_:didadd:to:)-4hiew.md)
  Tells the delegate that a home added a room to a zone.
- [func home(HMHome, didRemove: HMRoom, from: HMZone)](hmhomedelegate/home(_:didremove:from:)-8oz67.md)
  Tells the delegate that a home removed a room from a zone.
- [func home(HMHome, didRemove: HMRoom)](hmhomedelegate/home(_:didremove:)-3if6s.md)
  Tells the delegate that a home removed a room.
- [func home(HMHome, didAdd: HMZone)](hmhomedelegate/home(_:didadd:)-7vyoe.md)
  Tells the delegate that a home added a new zone.
- [func home(HMHome, didRemove: HMZone)](hmhomedelegate/home(_:didremove:)-3o8ta.md)
  Tells the delegate that a home removed a zone.
- [func home(HMHome, didAdd: HMUser)](hmhomedelegate/home(_:didadd:)-8q7jm.md)
  Tells the delegate that a home added a user.
- [func home(HMHome, didRemove: HMUser)](hmhomedelegate/home(_:didremove:)-3fm38.md)
  Tells the delegate that a home removed a user.
- [func homeDidUpdateAccessControl(forCurrentUser: HMHome)](hmhomedelegate/homedidupdateaccesscontrol(forcurrentuser:).md)
  Tells the delegate that the access control for the current user has changed.
- [func home(HMHome, didUpdate: HMHomeHubState)](hmhomedelegate/home(_:didupdate:)-5fntk.md)
  Tells the delegate that the state of the home hub has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didupdatenamefor:)-1k32g)*