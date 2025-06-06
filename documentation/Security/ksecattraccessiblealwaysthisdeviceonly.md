# kSecAttrAccessibleAlwaysThisDeviceOnly

**Framework**: Security  
**Kind**: var

The data in the keychain item can always be accessed regardless of whether the device is locked.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrAccessibleAlwaysThisDeviceOnly: CFString
```

#### Discussion

This is not recommended for application use. Items with this attribute  migrate to a new device. Thus, after restoring from a backup of a different device, these items will not be present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessiblealwaysthisdeviceonly)*