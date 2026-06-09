# allowsPersistentDNS

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether storing and usage of DNS answers in a persistent per-process cache is allowed.

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

This should only be set for hostnames whose resolutions are not expected to change across networks. Defaults to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/allowspersistentdns)*