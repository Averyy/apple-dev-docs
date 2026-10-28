# touchIDAny

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Constraint to access an item with Touch ID for any enrolled fingers.

**Availability**:
- iOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryAny)
- iPadOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryAny)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: SecAccessControlCreateFlags.biometryAny)
- macOS 10.12.1+ - Deprecated in 10.13.4 (renamed: SecAccessControlCreateFlags.biometryAny)
- tvOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryAny)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecAccessControlCreateFlags.biometryAny)
- watchOS 2.0+ - Deprecated in 4.3 (renamed: SecAccessControlCreateFlags.biometryAny)

> **Deprecated**: Use [`biometryAny`](./biometryany.md) instead.

## Declaration

```swift
static var touchIDAny: SecAccessControlCreateFlags { get }
```

```c
kSecAccessControlTouchIDAny
```

## Discussion

Touch ID must be available and enrolled with at least one finger. The item is still accessible by Touch ID if fingers are added or removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/touchidany)*