# WebDomainToken

**Framework**: ManagedSettings  
**Kind**: typealias

A representation of a web domain that preserves the user’s privacy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
typealias WebDomainToken = Token<WebDomain>
```

#### Discussion

Managed Settings uses representations of web domains to preserve user privacy and control. Use a token to represent a web domain without revealing what domain the token represents. [`FamilyActivitySelection`](https://developer.apple.com/documentation/FamilyControls/FamilyActivitySelection) provides tokens that devices within the same Family Sharing group can use to identify applications.

## See Also

- [struct WebDomain](webdomain.md)
  An object that represents a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webdomaintoken)*