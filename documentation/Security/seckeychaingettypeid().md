# SecKeychainGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a keychain object belongs.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainGetTypeID() -> CFTypeID
```

```c
CFTypeID SecKeychainGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecKeychain`](./seckeychain.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecKeychain`](./seckeychain.md) object. You can compare this value to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingettypeid())*