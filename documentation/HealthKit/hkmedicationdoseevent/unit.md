# unit

**Framework**: HealthKit  
**Kind**: property

The unit that the system associates with the medication when the person logs the dose.

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
var unit: HKUnit { get }
```

#### Discussion

This ensures that the dose quantity is recorded with the correct measurement unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/unit)*