# init(predicate:anchor:options:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(predicate: NSPredicate?, anchor: HKQueryAnchor?, options: HKWorkoutEffortRelationshipQueryOptions, resultsHandler: @escaping (HKWorkoutEffortRelationshipQuery, [HKWorkoutEffortRelationship]?, HKQueryAnchor?, (any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteffortrelationshipquery/init(predicate:anchor:options:resultshandler:))*