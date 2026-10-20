# MTRDeviceControllerStorageDelegate

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTRDeviceControllerStorageDelegate <NSObject>
```

## Topics

### Instance Methods
- [func controller(MTRDeviceController, removeValueForKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](./mtrdevicecontrollerstoragedelegate/controller%28_,removevalueforkey,securitylevel,sharingtype%29.md)
- [func controller(MTRDeviceController, storeValue: any NSSecureCoding, forKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](./mtrdevicecontrollerstoragedelegate/controller%28_,storevalue,forkey,securitylevel,sharingtype%29.md)
- [func controller(MTRDeviceController, storeValues: [String : any NSSecureCoding], securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool](./mtrdevicecontrollerstoragedelegate/controller%28_,storevalues,securitylevel,sharingtype%29.md)
- [func controller(MTRDeviceController, valueForKey: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> (any NSSecureCoding)?](./mtrdevicecontrollerstoragedelegate/controller%28_,valueforkey,securitylevel,sharingtype%29.md)
- [func values(for: MTRDeviceController, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> [String : any NSSecureCoding]?](./mtrdevicecontrollerstoragedelegate/values%28for,securitylevel,sharingtype%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate)*