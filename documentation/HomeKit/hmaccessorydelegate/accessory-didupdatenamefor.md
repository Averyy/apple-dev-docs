# accessory(_:didUpdateNameFor:)

**Framework**: HomeKit  
**Kind**: method

Informs the delegate when the name of a service is updated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func accessory(_ accessory: HMAccessory, didUpdateNameFor service: HMService)
```

## Parameters

- `accessory`: The accessory with an updated service name.
- `service`: The service whose name changed.

## See Also

- [func accessoryDidUpdateName(HMAccessory)](hmaccessorydelegate/accessorydidupdatename(_:).md)
  Informs the delegate when the name of the accessory is updated.
- [func accessoryDidUpdateReachability(HMAccessory)](hmaccessorydelegate/accessorydidupdatereachability(_:).md)
  Informs the delegate when the reachability of the accessory changes.
- [func accessoryDidUpdateServices(HMAccessory)](hmaccessorydelegate/accessorydidupdateservices(_:).md)
  Informs the delegate when the services on the accessory have been updated.
- [func accessory(HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)](hmaccessorydelegate/accessory(_:service:didupdatevaluefor:).md)
  Informs the delegate of a change in value of a characteristic.
- [func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](hmaccessorydelegate/accessory(_:didupdateassociatedservicetypefor:).md)
  Informs the delegate when the associated service type of a service is modified.
- [func accessory(HMAccessory, didAdd: HMAccessoryProfile)](hmaccessorydelegate/accessory(_:didadd:).md)
  Informs the delegate when a profile is added to an accessory.
- [func accessory(HMAccessory, didRemove: HMAccessoryProfile)](hmaccessorydelegate/accessory(_:didremove:).md)
  Informs the delegate when a profile is removed from an accessory.
- [func accessory(HMAccessory, didUpdateFirmwareVersion: String)](hmaccessorydelegate/accessory(_:didupdatefirmwareversion:).md)
  Informs the delegate when firmwareVersion has been changed for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/accessory(_:didupdatenamefor:))*