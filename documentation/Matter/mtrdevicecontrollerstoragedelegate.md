# MTRDeviceControllerStorageDelegate

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
protocol MTRDeviceControllerStorageDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func controller(MTRDeviceController, removeValueForKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](mtrdevicecontrollerstoragedelegate/controller(_:removevalueforkey:securitylevel:sharingtype:).md)
- [func controller(MTRDeviceController, storeValue: any NSSecureCoding, forKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](mtrdevicecontrollerstoragedelegate/controller(_:storevalue:forkey:securitylevel:sharingtype:).md)
- [func controller(MTRDeviceController, storeValues: [String : any NSSecureCoding], securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](mtrdevicecontrollerstoragedelegate/controller(_:storevalues:securitylevel:sharingtype:).md)
- [func controller(MTRDeviceController, valueForKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> (any NSSecureCoding)?](mtrdevicecontrollerstoragedelegate/controller(_:valueforkey:securitylevel:sharingtype:).md)
- [func values(for: MTRDeviceController, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> [String : any NSSecureCoding]?](mtrdevicecontrollerstoragedelegate/values(for:securitylevel:sharingtype:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate)*