# kSecMatchLimit

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the match limit.

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
let kSecMatchLimit: CFString
```

```c
extern CFStringRef const kSecMatchLimit;
```

## Mentions

- [Searching for keychain items](./searching-for-keychain-items.md)
- [Storing Keys in the Keychain](./storing-keys-in-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFNumber`](../CoreFoundation/cfnumber.md). If provided, this value specifies the maximum number of results to return or otherwise act upon. For a single item, specify [`kSecMatchLimitOne`](./ksecmatchlimitone.md). To specify all matching items, specify [`kSecMatchLimitAll`](./ksecmatchlimitall.md). The default behavior is function-dependent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchlimit)*