# kSecAttrSynchronizableAny

**Framework**: Security  
**Kind**: var

Specifies that both synchronizable and non-synchronizable results should be returned from a query.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrSynchronizableAny: CFString
```

#### Discussion

This may be used as a value for the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) dictionary key (in place of `kCFBooleanTrue` or `kCFBooleanFalse`) in a call to [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md), [`SecItemUpdate(_:_:)`](secitemupdate(_:_:).md), or [`SecItemDelete(_:)`](secitemdelete(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)*