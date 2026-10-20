# controller(_:storeValue:forKey:securityLevel:sharingType:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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
func controller(_ controller: MTRDeviceController, storeValue value: any NSSecureCoding, forKey key: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> Bool
```

```objc
- (BOOL) controller:(MTRDeviceController *) controller storeValue:(id<NSSecureCoding>) value forKey:(NSString *) key securityLevel:(MTRStorageSecurityLevel) securityLevel sharingType:(MTRStorageSharingType) sharingType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate/controller(_:storevalue:forkey:securitylevel:sharingtype:))*