# kSecMatchSearchList

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates a list of items to search.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecMatchSearchList: CFString
```

```c
extern CFStringRef const kSecMatchSearchList;
```

#### Discussion

The value is a [`CFArray`](../CoreFoundation/cfarray.md) of [`SecKeychain`](./seckeychain.md) items. If provided, the search will be limited to the keychain items contained in this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchsearchlist)*