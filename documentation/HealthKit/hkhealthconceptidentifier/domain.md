# domain

**Framework**: HealthKit  
**Kind**: property

The domain this identifier belongs to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var domain: HKHealthConceptDomain { get }
```

#### Discussion

This value identifies the group of concepts the identifier comes from. For example, if the identifier represents a medication, the category will be the medication domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthconceptidentifier/domain)*