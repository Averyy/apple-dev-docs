# touchIDCurrentSet

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Constraint to access an item with Touch ID for currently enrolled fingers.

**Availability**:
- iOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- iPadOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- macOS 10.12.1+ - Deprecated in 10.13.4 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- tvOS 9.0+ - Deprecated in 11.3 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)
- watchOS 2.0+ - Deprecated in 4.3 (renamed: SecAccessControlCreateFlags.biometryCurrentSet)

> **Deprecated**: Use [`biometryCurrentSet`](./biometrycurrentset.md) instead.

## Declaration

```swift
static var touchIDCurrentSet: SecAccessControlCreateFlags { get }
```

```c
kSecAccessControlTouchIDCurrentSet
```

#### Discussion

Touch ID must be available and enrolled with at least one finger. The item is invalidated if fingers are added or removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/touchidcurrentset)*