# HKAnchoredObjectQueryNoAnchor

**Framework**: HealthKit  
**Kind**: var

An anchor that returns all of the matching samples currently in the HealthKit store.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var HKAnchoredObjectQueryNoAnchor: Int32 { get }
```

#### Discussion

> ❗ **Important**:  Only use this constant to support iOS 8 (using the deprecated [`init(type:predicate:anchor:limit:completionHandler:)`](hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:).md) method). In iOS 9 and later, use [`init(type:predicate:anchor:limit:resultsHandler:)`](hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:).md) and pass `nil` instead.

Use this constant the first time you perform an anchored object query. The resulting query returns all the matching samples currently in the HealthKit store. For subsequent anchored object queries, use the anchor returned by the previous query. The resulting query returns only samples that have been added to the HealthKit store since the previous query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerynoanchor)*