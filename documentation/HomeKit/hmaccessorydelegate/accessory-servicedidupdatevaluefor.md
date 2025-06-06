# accessory(_:service:didUpdateValueFor:)

**Framework**: HomeKit  
**Kind**: method

Informs the delegate of a change in value of a characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func accessory(_ accessory: HMAccessory, service: HMService, didUpdateValueFor characteristic: HMCharacteristic)
```

## Mentions

- [Testing your app with the HomeKit Accessory Simulator](testing-your-app-with-the-homekit-accessory-simulator.md)

#### Discussion

This method is called as a result of a change in value initiated by the accessory. Programmatic changes initiated by the app do not result in this method being called.

## Parameters

- `accessory`: The accessory.
- `service`: The service with a changed characteristic value.
- `characteristic`: The characteristic whose value changed.

## See Also

- [func accessoryDidUpdateName(HMAccessory)](hmaccessorydelegate/accessorydidupdatename(_:).md)
  Informs the delegate when the name of the accessory is updated.
- [func accessoryDidUpdateReachability(HMAccessory)](hmaccessorydelegate/accessorydidupdatereachability(_:).md)
  Informs the delegate when the reachability of the accessory changes.
- [func accessoryDidUpdateServices(HMAccessory)](hmaccessorydelegate/accessorydidupdateservices(_:).md)
  Informs the delegate when the services on the accessory have been updated.
- [func accessory(HMAccessory, didUpdateNameFor: HMService)](hmaccessorydelegate/accessory(_:didupdatenamefor:).md)
  Informs the delegate when the name of a service is updated.
- [func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](hmaccessorydelegate/accessory(_:didupdateassociatedservicetypefor:).md)
  Informs the delegate when the associated service type of a service is modified.
- [func accessory(HMAccessory, didAdd: HMAccessoryProfile)](hmaccessorydelegate/accessory(_:didadd:).md)
  Informs the delegate when a profile is added to an accessory.
- [func accessory(HMAccessory, didRemove: HMAccessoryProfile)](hmaccessorydelegate/accessory(_:didremove:).md)
  Informs the delegate when a profile is removed from an accessory.
- [func accessory(HMAccessory, didUpdateFirmwareVersion: String)](hmaccessorydelegate/accessory(_:didupdatefirmwareversion:).md)
  Informs the delegate when firmwareVersion has been changed for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/accessory(_:service:didupdatevaluefor:))*