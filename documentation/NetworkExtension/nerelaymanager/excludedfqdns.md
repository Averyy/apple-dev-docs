# excludedFQDNs

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var excludedFQDNs: [String]? { get set }
```

#### Discussion

An array of strings containing Fully Qualified Domain Names (FQDNs). If the destination host matches one of these strings then the relay will not be used.  An excluded FQDN takes priority over the matchDomain property.  This means the relay will not be used if the hostname matches an FQDN in this array even if the matchDomains contains a domain that would have been considered a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/excludedfqdns)*