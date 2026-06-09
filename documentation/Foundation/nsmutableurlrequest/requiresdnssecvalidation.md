# requiresDNSSECValidation

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether a request requires DNSSEC validation during DNS lookup.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
var requiresDNSSECValidation: Bool { get set }
```

#### Discussion

`YES` if the DNS lookup for this request should require DNSSEC validation. Defaults to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/requiresdnssecvalidation)*