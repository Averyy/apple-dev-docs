# userPresence

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Constraint to access an item with either biometry or passcode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var userPresence: SecAccessControlCreateFlags { get }
```

```c
kSecAccessControlUserPresence
```

## Mentions

- [Restricting keychain item accessibility](../restricting-keychain-item-accessibility.md)

#### Discussion

Biometry doesn’t have to be available or enrolled. The item is still accessible by Touch ID even if fingers are added or removed, or by Face ID if the user is re-enrolled.

This option is equivalent to specifying [`biometryAny`](./biometryany.md), [`or`](./or.md), and [`devicePasscode`](./devicepasscode.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/userpresence)*