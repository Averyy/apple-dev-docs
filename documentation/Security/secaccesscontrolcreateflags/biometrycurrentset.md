# biometryCurrentSet

**Framework**: Security  
**Kind**: property

Constraint to access an item with Touch ID for currently enrolled fingers, or from Face ID with the currently enrolled user.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
static var biometryCurrentSet: SecAccessControlCreateFlags { get }
```

#### Discussion

Touch ID must be available and enrolled with at least one finger, or Face ID available and enrolled. The item is invalidated if fingers are added or removed for Touch ID, or if the user re-enrolls for Face ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/biometrycurrentset)*