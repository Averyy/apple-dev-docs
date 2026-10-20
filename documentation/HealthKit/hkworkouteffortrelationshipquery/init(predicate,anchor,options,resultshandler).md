# init(predicate:anchor:options:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(predicate: NSPredicate?, anchor: HKQueryAnchor?, options: HKWorkoutEffortRelationshipQueryOptions, resultsHandler: @escaping @Sendable (HKWorkoutEffortRelationshipQuery, [HKWorkoutEffortRelationship]?, HKQueryAnchor?, (any Error)?) -> Void)
```

```objc
- (instancetype) initWithPredicate:(NSPredicate *) predicate anchor:(HKQueryAnchor *) anchor options:(HKWorkoutEffortRelationshipQueryOptions) options resultsHandler:(void (^)(HKWorkoutEffortRelationshipQuery *query, NSArray<HKWorkoutEffortRelationship *> *relationships, HKQueryAnchor *newAnchor, NSError *error)) resultsHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouteffortrelationshipquery/init(predicate:anchor:options:resultshandler:))*