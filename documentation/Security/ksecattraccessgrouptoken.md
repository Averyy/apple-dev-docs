# kSecAttrAccessGroupToken

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The access group containing items provided by external tokens.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let kSecAttrAccessGroupToken: CFString
```

```c
extern CFStringRef const kSecAttrAccessGroupToken;
```

#### Discussion

Use this access group identifier as the value for the [`kSecAttrAccessGroup`](./ksecattraccessgroup.md) attribute in a keychain query to access external tokens such as smart cards. Access to this group is granted by default and does not require an explicit entry in your app’s [`Keychain Access Groups Entitlement`](../BundleResources/entitlements/keychain-access-groups.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessgrouptoken)*