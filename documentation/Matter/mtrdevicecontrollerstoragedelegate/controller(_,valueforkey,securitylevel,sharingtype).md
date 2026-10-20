# controller(_:valueForKey:securityLevel:sharingType:)

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
func controller(_ controller: MTRDeviceController, valueForKey key: String, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> (any NSSecureCoding)?
```

```objc
- (id<NSSecureCoding>) controller:(MTRDeviceController *) controller valueForKey:(NSString *) key securityLevel:(MTRStorageSecurityLevel) securityLevel sharingType:(MTRStorageSharingType) sharingType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate/controller(_:valueforkey:securitylevel:sharingtype:))*