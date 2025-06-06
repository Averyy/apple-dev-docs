# HMHomeManagerDelegate

**Framework**: HomeKit  
**Kind**: protocol

An interface the home manager uses to communicate changes to the state of the home network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol HMHomeManagerDelegate : NSObjectProtocol
```

#### Overview

Adopt this protocol to find out about changes made outside your app to the set of homes in the HomeKit database, like when homes are added or removed by another app. You also rely on this protocol when you first create an [`HMHomeManager`](hmhomemanager.md) instance. The home manager calls the [`homeManagerDidUpdateHomes(_:)`](hmhomemanagerdelegate/homemanagerdidupdatehomes(_:).md) method to indicate that it has finished its initial load of data from the HomeKit database.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To be alerted about changes made within a particular home, adopt the [`HMHomeDelegate`](hmhomedelegate.md) protocol. To find out about changes made to specific accessories, adopt the [`HMAccessoryDelegate`](hmaccessorydelegate.md) protocol.

## Topics

### Adding and removing homes
- [func homeManagerDidUpdateHomes(HMHomeManager)](hmhomemanagerdelegate/homemanagerdidupdatehomes(_:).md)
  Tells the delegate that the home manager updated its collection of homes.
- [func homeManager(HMHomeManager, didAdd: HMHome)](hmhomemanagerdelegate/homemanager(_:didadd:).md)
  Tells the delegate that the home manager added a home.
- [func homeManager(HMHomeManager, didRemove: HMHome)](hmhomemanagerdelegate/homemanager(_:didremove:).md)
  Tells the delegate that the home manager removed a home.
- [func homeManagerDidUpdatePrimaryHome(HMHomeManager)](hmhomemanagerdelegate/homemanagerdidupdateprimaryhome(_:).md)
  Tells the delegate that the home manager updated its primary home.
### Adding accessories
- [func homeManager(HMHomeManager, didReceiveAddAccessoryRequest: HMAddAccessoryRequest)](hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:).md)
  Tells the delegate to add an accessory to a home by using a setup payload.
- [class HMAddAccessoryRequest](hmaddaccessoryrequest.md)
  A request to add an accessory to a particular home.
### Monitoring authorization status
- [func homeManager(HMHomeManager, didUpdate: HMHomeManagerAuthorizationStatus)](hmhomemanagerdelegate/homemanager(_:didupdate:).md)
  Tells the delegate when the authorization status changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMHomeManagerDelegate)?](hmhomemanager/delegate.md)
  A delegate that receives updates on the collection of homes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate)*