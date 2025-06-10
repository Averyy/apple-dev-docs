# execute(_:)

**Framework**: HealthKit  
**Kind**: method

Starts executing the provided query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func execute(_ query: HKQuery)
```

## Mentions

- [Executing Statistical Queries](executing-statistical-queries.md)
- [Executing Activity Summary Queries](executing-activity-summary-queries.md)
- [Executing Source Queries](executing-source-queries.md)
- [Executing Observer Queries](executing-observer-queries.md)
- [Executing Anchored Object Queries](executing-anchored-object-queries.md)
- [Reading route data](reading-route-data.md)
- [Executing Sample Queries](executing-sample-queries.md)

#### Discussion

HealthKit executes queries asynchronously on a background queue. Most queries automatically stop after they have finished executing. However, long-running queries—such as observer queries and some statistics collection queries—continue to execute in the background. To stop long-running queries, call the [`stop(_:)`](hkhealthstore/stop(_:).md) method.

## Parameters

- `query`: A concrete subclass of the   class (any of the classes  ,  ,  ,  ,  ,  , or  ).

## See Also

- [func stop(HKQuery)](hkhealthstore/stop(_:).md)
  Stops a long-running query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/execute(_:))*