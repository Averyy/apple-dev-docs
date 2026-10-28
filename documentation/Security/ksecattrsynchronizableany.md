# kSecAttrSynchronizableAny

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kSecAttrSynchronizableAny;
```

## Discussion

This may be used as a value for the [`kSecAttrSynchronizable`](./ksecattrsynchronizable.md) dictionary key (in place of `kCFBooleanTrue` or `kCFBooleanFalse`) in a call to [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md), [`SecItemUpdate(_:_:)`](./secitemupdate%28_,_%29.md), or [`SecItemDelete(_:)`](./secitemdelete%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)*