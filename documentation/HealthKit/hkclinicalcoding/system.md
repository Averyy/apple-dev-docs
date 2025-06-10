# system

**Framework**: HealthKit  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var system: String { get }
```

#### Discussion

In most cases, it will be the canonical reference URL for the coding system with respect to the HL7 Terminology. For the system RxNorm, for example, this would be “http://www.nlm.nih.gov/research/umls/rxnorm”, according to https://terminology.hl7.org/CodeSystem-v3-rxNorm.html.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding/system)*