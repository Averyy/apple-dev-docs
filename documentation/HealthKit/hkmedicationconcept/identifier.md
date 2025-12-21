# identifier

**Framework**: HealthKit  
**Kind**: property

The unique identifier for the specific medication concept.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@NSCopying
var identifier: HKHealthConceptIdentifier { get }
```

#### Discussion

Each concept has one stable identifier that stays the same across devices. You can use this identifier to directly compare medications, for example, to check whether two objects represent the same medication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationconcept/identifier)*