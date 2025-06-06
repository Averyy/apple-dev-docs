# accessory(_:didRemove:)

**Framework**: HomeKit  
**Kind**: method

Informs the delegate when a profile is removed from an accessory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func accessory(_ accessory: HMAccessory, didRemove profile: HMAccessoryProfile)
```

## Parameters

- `accessory`: The accessory from which the profile is removed.
- `profile`: The removed profile.

## See Also

- [func accessoryDidUpdateName(HMAccessory)](hmaccessorydelegate/accessorydidupdatename(_:).md)
  Informs the delegate when the name of the accessory is updated.
- [func accessoryDidUpdateReachability(HMAccessory)](hmaccessorydelegate/accessorydidupdatereachability(_:).md)
  Informs the delegate when the reachability of the accessory changes.
- [func accessoryDidUpdateServices(HMAccessory)](hmaccessorydelegate/accessorydidupdateservices(_:).md)
  Informs the delegate when the services on the accessory have been updated.
- [func accessory(HMAccessory, didUpdateNameFor: HMService)](hmaccessorydelegate/accessory(_:didupdatenamefor:).md)
  Informs the delegate when the name of a service is updated.
- [func accessory(HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)](hmaccessorydelegate/accessory(_:service:didupdatevaluefor:).md)
  Informs the delegate of a change in value of a characteristic.
- [func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](hmaccessorydelegate/accessory(_:didupdateassociatedservicetypefor:).md)
  Informs the delegate when the associated service type of a service is modified.
- [func accessory(HMAccessory, didAdd: HMAccessoryProfile)](hmaccessorydelegate/accessory(_:didadd:).md)
  Informs the delegate when a profile is added to an accessory.
- [func accessory(HMAccessory, didUpdateFirmwareVersion: String)](hmaccessorydelegate/accessory(_:didupdatefirmwareversion:).md)
  Informs the delegate when firmwareVersion has been changed for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/accessory(_:didremove:))*