# applicationPassword

**Framework**: Security  
**Kind**: property

Option to use an application-provided password for data encryption key generation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var applicationPassword: SecAccessControlCreateFlags { get }
```

## Mentions

- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)

#### Discussion

This may be specified in addition to any constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/applicationpassword)*