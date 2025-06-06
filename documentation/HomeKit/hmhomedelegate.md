# HMHomeDelegate

**Framework**: HomeKit  
**Kind**: protocol

An interface that communicates changes to a home’s configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol HMHomeDelegate : NSObjectProtocol
```

#### Overview

Adopt this protocol to find out about changes made outside your app to a particular home, like when the home’s name changes, or when a room is added.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To be alerted about changes made to the overall list of homes, adopt the [`HMHomeManagerDelegate`](hmhomemanagerdelegate.md) protocol. To find out about changes made to specific accessories, adopt the [`HMAccessoryDelegate`](hmaccessorydelegate.md) protocol.

## Topics

### Observing Home Configuration
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
- [func home(HMHome, didUpdateNameFor: HMZone)](hmhomedelegate/home(_:didupdatenamefor:)-1k32g.md)
  Tells the delegate that a home changed the name of a zone.
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
- [func homeDidUpdateSupportedFeatures(HMHome)](hmhomedelegate/homedidupdatesupportedfeatures(_:).md)
  Tells the delegate that the home’s supported features changed.
- [enum HMHomeHubState](hmhomehubstate.md)
  The possible states of the home hub.
### Observing Service Configuration
- [func home(HMHome, didAdd: HMServiceGroup)](hmhomedelegate/home(_:didadd:)-3dymz.md)
  Tells the delegate that a home added a service group.
- [func home(HMHome, didUpdateNameFor: HMServiceGroup)](hmhomedelegate/home(_:didupdatenamefor:)-4tam1.md)
  Tells the delegate that a home updated the name of a service group.
- [func home(HMHome, didAdd: HMService, to: HMServiceGroup)](hmhomedelegate/home(_:didadd:to:)-6xdgy.md)
  Tells the delegate that a home added a service to a service group.
- [func home(HMHome, didRemove: HMService, from: HMServiceGroup)](hmhomedelegate/home(_:didremove:from:)-9yzp0.md)
  Tells the delegate that a home removed a service from a service group.
- [func home(HMHome, didRemove: HMServiceGroup)](hmhomedelegate/home(_:didremove:)-6kqxo.md)
  Tells the delegate that a home removed a service group.
### Observing Action and Trigger Configuration
- [func home(HMHome, didAdd: HMActionSet)](hmhomedelegate/home(_:didadd:)-9dcki.md)
  Tells the delegate that a home added an action set.
- [func home(HMHome, didUpdateNameFor: HMActionSet)](hmhomedelegate/home(_:didupdatenamefor:)-7fxvl.md)
  Tells the delegate that a home updated the name of an action set.
- [func home(HMHome, didUpdateActionsFor: HMActionSet)](hmhomedelegate/home(_:didupdateactionsfor:).md)
  Tells the delegate that a home updated the actions for an action set.
- [func home(HMHome, didRemove: HMActionSet)](hmhomedelegate/home(_:didremove:)-80ewx.md)
  Tells the delegate that a home removed an action set.
- [func home(HMHome, didAdd: HMTrigger)](hmhomedelegate/home(_:didadd:)-64yxx.md)
  Tells the delegate that a home added a trigger.
- [func home(HMHome, didUpdateNameFor: HMTrigger)](hmhomedelegate/home(_:didupdatenamefor:)-8vn79.md)
  Tells the delegate that a home updated the name of a trigger.
- [func home(HMHome, didUpdate: HMTrigger)](hmhomedelegate/home(_:didupdate:)-3l4r1.md)
  Tells the delegate that a home updated a trigger.
- [func home(HMHome, didRemove: HMTrigger)](hmhomedelegate/home(_:didremove:)-4ujfa.md)
  Tells the delegate that a home removed a trigger.
### Observing Accessories
- [func home(HMHome, didEncounterError: any Error, for: HMAccessory)](hmhomedelegate/home(_:didencountererror:for:).md)
  Tells the delegate that a configured accessory encountered an error.
- [func home(HMHome, didUnblockAccessory: HMAccessory)](hmhomedelegate/home(_:didunblockaccessory:).md)
  Tells the delegate that an accessory has been unblocked.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMHomeDelegate)?](hmhome/delegate.md)
  A delegate that receives updates on the state of the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate)*