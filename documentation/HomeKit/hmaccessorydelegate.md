# HMAccessoryDelegate

**Framework**: HomeKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that defines the communication method for state updates from accessories to their delegates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol HMAccessoryDelegate : NSObjectProtocol, Sendable
```

```objc
@protocol HMAccessoryDelegate <NSObject>
```

#### Overview

Adopt this protocol to find out about changes made outside your app to a specific accessory, like when the accessory’s name changes, or when a characteristic value changes.

> **Note**:  To receive [`accessory(_:service:didUpdateValueFor:)`](./hmaccessorydelegate/accessory%28_,service,didupdatevaluefor%29.md) method calls for a particular characteristic, indicating when the characteristic value changes, you must first call the characteristic’s [`enableNotification(_:completionHandler:)`](./hmcharacteristic/enablenotification%28_,completionhandler%29.md) method.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To find out about changes made to the accessory’s home, adopt the [`HMHomeDelegate`](./hmhomedelegate.md) protocol. To be alerted about changes made to the overall list of homes, adopt the [`HMHomeManagerDelegate`](./hmhomemanagerdelegate.md) protocol.

## Topics

### Observing accessories
- [func accessoryDidUpdateName(HMAccessory)](./hmaccessorydelegate/accessorydidupdatename%28_%29.md)
  Informs the delegate when the name of the accessory is updated.
- [func accessoryDidUpdateReachability(HMAccessory)](./hmaccessorydelegate/accessorydidupdatereachability%28_%29.md)
  Informs the delegate when the reachability of the accessory changes.
- [func accessoryDidUpdateServices(HMAccessory)](./hmaccessorydelegate/accessorydidupdateservices%28_%29.md)
  Informs the delegate when the services on the accessory have been updated.
- [func accessory(HMAccessory, didUpdateNameFor: HMService)](./hmaccessorydelegate/accessory%28_,didupdatenamefor%29.md)
  Informs the delegate when the name of a service is updated.
- [func accessory(HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)](./hmaccessorydelegate/accessory%28_,service,didupdatevaluefor%29.md)
  Informs the delegate of a change in value of a characteristic.
- [func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](./hmaccessorydelegate/accessory%28_,didupdateassociatedservicetypefor%29.md)
  Informs the delegate when the associated service type of a service is modified.
- [func accessory(HMAccessory, didAdd: HMAccessoryProfile)](./hmaccessorydelegate/accessory%28_,didadd%29.md)
  Informs the delegate when a profile is added to an accessory.
- [func accessory(HMAccessory, didRemove: HMAccessoryProfile)](./hmaccessorydelegate/accessory%28_,didremove%29.md)
  Informs the delegate when a profile is removed from an accessory.
- [func accessory(HMAccessory, didUpdateFirmwareVersion: String)](./hmaccessorydelegate/accessory%28_,didupdatefirmwareversion%29.md)
  Informs the delegate when firmwareVersion has been changed for an accessory.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tracking changes to an accessory
- [var delegate: (any HMAccessoryDelegate)?](./hmaccessory/delegate.md)
  A delegate that receives updates on the state of the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorydelegate)*