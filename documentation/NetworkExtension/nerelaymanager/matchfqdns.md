# matchFQDNs

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
var matchFQDNs: [String]? { get set }
```

#### Discussion

An array of strings containing Fully Qualified Domain Names (FQDNs). If this property is non-nil, the relay will be used to access the specified hosts.  If this and the matchDomains property is nil, the relay will be used for all domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/matchfqdns)*