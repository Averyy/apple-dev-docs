# requiresDNSSECValidation

**Framework**: Foundation  
**Kind**: property

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
var requiresDNSSECValidation: Bool { get }
```

#### Discussion

Sets whether a request is required to do DNSSEC validation during DNS lookup.

YES, if the DNS lookup for this request should require DNSSEC validation, No otherwise. Defaults to NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/requiresdnssecvalidation)*