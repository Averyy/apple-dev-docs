# kSecAttrAccessControl

**Framework**: Security  
**Kind**: var

A key with a value that’s an access control instance indicating access control settings for the item.

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
let kSecAttrAccessControl: CFString
```

## Mentions

- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)

#### Discussion

The corresponding value is a [`SecAccessControl`](secaccesscontrol.md) instance, created with the [`SecAccessControlCreateWithFlags(_:_:_:_:)`](secaccesscontrolcreatewithflags(_:_:_:_:).md) method, containing access control conditions for the item. See [`Restricting keychain item accessibility`](restricting-keychain-item-accessibility.md) for more details.

> ❗ **Important**:  This attribute is mutually exclusive with the [`kSecAttrAccess`](ksecattraccess.md) attribute.

 This attribute is mutually exclusive with the [`kSecAttrAccess`](ksecattraccess.md) attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccesscontrol)*