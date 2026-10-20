# homeDidUpdateSupportedFeatures(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the home’s supported features changed.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- tvOS 13.2+
- visionOS 1.0+
- watchOS 6.1+

## Declaration

```swift
optional func homeDidUpdateSupportedFeatures(_ home: HMHome)
```

```objc
- (void) homeDidUpdateSupportedFeatures:(HMHome *) home;
```

## Parameters

- `home`: The home for which supported features changed.

## See Also

### Observing Home Configuration
- [func homeDidUpdateName(HMHome)](./homedidupdatename%28_%29.md)
  Tells the delegate that a home’s name changed.
- [func home(HMHome, didAdd: HMAccessory)](./home%28_,didadd%29-6jcl7.md)
  Tells the delegate that a home added a new accessory.
- [func home(HMHome, didUpdate: HMRoom, for: HMAccessory)](./home%28_,didupdate,for%29.md)
  Tells the delegate that a home assigned an accessory to a different room.
- [func home(HMHome, didRemove: HMAccessory)](./home%28_,didremove%29-6plye.md)
  Tells the delegate that a home removed an accessory.
- [func home(HMHome, didAdd: HMRoom)](./home%28_,didadd%29-42aqd.md)
  Tells the delegate that a home added a new room.
- [func home(HMHome, didUpdateNameFor: HMRoom)](./home%28_,didupdatenamefor%29-1a110.md)
  Tells the delegate that a home updated the name of one of its rooms.
- [func home(HMHome, didAdd: HMRoom, to: HMZone)](./home%28_,didadd,to%29-4hiew.md)
  Tells the delegate that a home added a room to a zone.
- [func home(HMHome, didRemove: HMRoom, from: HMZone)](./home%28_,didremove,from%29-8oz67.md)
  Tells the delegate that a home removed a room from a zone.
- [func home(HMHome, didRemove: HMRoom)](./home%28_,didremove%29-3if6s.md)
  Tells the delegate that a home removed a room.
- [func home(HMHome, didAdd: HMZone)](./home%28_,didadd%29-7vyoe.md)
  Tells the delegate that a home added a new zone.
- [func home(HMHome, didUpdateNameFor: HMZone)](./home%28_,didupdatenamefor%29-1k32g.md)
  Tells the delegate that a home changed the name of a zone.
- [func home(HMHome, didRemove: HMZone)](./home%28_,didremove%29-3o8ta.md)
  Tells the delegate that a home removed a zone.
- [func home(HMHome, didAdd: HMUser)](./home%28_,didadd%29-8q7jm.md)
  Tells the delegate that a home added a user.
- [func home(HMHome, didRemove: HMUser)](./home%28_,didremove%29-3fm38.md)
  Tells the delegate that a home removed a user.
- [func homeDidUpdateAccessControl(forCurrentUser: HMHome)](./homedidupdateaccesscontrol%28forcurrentuser%29.md)
  Tells the delegate that the access control for the current user has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/homedidupdatesupportedfeatures(_:))*