# kSecUseUserIndependentKeychain

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key with a value that indicates whether to store the data in a keychain available to anyone who uses the device.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
let kSecUseUserIndependentKeychain: CFString
```

```c
extern CFStringRef const kSecUseUserIndependentKeychain;
```

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). A value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) stores the item in a shared keychain that your app can access even when a different user is active. A value of [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) or omitting this key-value pair stores the item in the current user’s keychain.

To view a sample code project that uses this key to streamline experiences like family media accounts, see [Mapping Apple TV users to app profiles](../TVServices/mapping-apple-tv-users-to-app-profiles.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseuserindependentkeychain)*