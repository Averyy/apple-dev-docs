# values(for:securityLevel:sharingType:)

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
optional func values(for controller: MTRDeviceController, securityLevel: MTRStorageSecurityLevel, sharingType: MTRStorageSharingType) -> [String : any NSSecureCoding]?
```

```objc
- (NSDictionary<NSString *,id<NSSecureCoding>> *) valuesForController:(MTRDeviceController *) controller securityLevel:(MTRStorageSecurityLevel) securityLevel sharingType:(MTRStorageSharingType) sharingType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstoragedelegate/values(for:securitylevel:sharingtype:))*