# controller(_:storeValues:securityLevel:sharingType:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
optional func controller(_ controller: MTRDeviceController, storeValues values: [String : any NSSecureCoding], securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool
```

```objc
- (BOOL) controller:(MTRDeviceController *) controller storeValues:(NSDictionary<NSString *,id<NSSecureCoding>> *) values securityLevel:(MTRStorageSecurityLevel) securityLevel sharingType:(MTRStorageSharingType) sharingType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate/controller(_:storevalues:securitylevel:sharingtype:))*