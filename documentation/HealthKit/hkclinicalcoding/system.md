# system

**Framework**: HealthKit  
**Kind**: property

The string that identifies the coding system that defines this clinical code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var system: String { get }
```

#### Discussion

The system is usually expressed as a URL from the [`HL7 Terminology`](https://developer.apple.comhttps://terminology.hl7.org/). For example, the RxNorm, a coding system for medications uses: `http://www.nlm.nih.gov/research/umls/rxnorm`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding/system)*