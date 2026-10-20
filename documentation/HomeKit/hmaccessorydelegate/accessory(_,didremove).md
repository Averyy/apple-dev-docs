# accessory(_:didRemove:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) accessory:(HMAccessory *) accessory didRemoveProfile:(HMAccessoryProfile *) profile;
```

## Parameters

- `accessory`: The accessory from which the profile is removed.
- `profile`: The removed profile.

## See Also

### Observing accessories
- [func accessoryDidUpdateName(HMAccessory)](./accessorydidupdatename%28_%29.md)
  Informs the delegate when the name of the accessory is updated.
- [func accessoryDidUpdateReachability(HMAccessory)](./accessorydidupdatereachability%28_%29.md)
  Informs the delegate when the reachability of the accessory changes.
- [func accessoryDidUpdateServices(HMAccessory)](./accessorydidupdateservices%28_%29.md)
  Informs the delegate when the services on the accessory have been updated.
- [func accessory(HMAccessory, didUpdateNameFor: HMService)](./accessory%28_,didupdatenamefor%29.md)
  Informs the delegate when the name of a service is updated.
- [func accessory(HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)](./accessory%28_,service,didupdatevaluefor%29.md)
  Informs the delegate of a change in value of a characteristic.
- [func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)](./accessory%28_,didupdateassociatedservicetypefor%29.md)
  Informs the delegate when the associated service type of a service is modified.
- [func accessory(HMAccessory, didAdd: HMAccessoryProfile)](./accessory%28_,didadd%29.md)
  Informs the delegate when a profile is added to an accessory.
- [func accessory(HMAccessory, didUpdateFirmwareVersion: String)](./accessory%28_,didupdatefirmwareversion%29.md)
  Informs the delegate when firmwareVersion has been changed for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/accessory(_:didremove:))*