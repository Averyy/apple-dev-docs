# allowsPersistentDNS

**Framework**: Foundation  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var allowsPersistentDNS: Bool { get }
```

#### Discussion

Allows storing and usage of DNS answers, potentially beyond TTL expiry, in a persistent per-process cache. This should only be set for hostnames whose resolutions are not expected to change across networks.

YES, if the DNS lookup for this request is allowed to use a persistent per-process cache, NO otherwise. Defaults to NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/allowspersistentdns)*