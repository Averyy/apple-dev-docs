# kSecAttrAccessibleAlways

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The data in the keychain item can always be accessed regardless of whether the device is locked.

**Availability**:
- iOS 4.0+ - Deprecated in 12.0
- iPadOS 4.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 5.0

> **Deprecated**: Use an accessibility level that provides some user protection, such as kSecAttrAccessibleAfterFirstUnlock

## Declaration

```swift
let kSecAttrAccessibleAlways: CFString
```

```c
extern CFStringRef const kSecAttrAccessibleAlways;
```

## Discussion

This is not recommended for application use. Items with this attribute migrate to a new device when using encrypted backups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessiblealways)*