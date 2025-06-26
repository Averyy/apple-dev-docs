# stop(_:)

**Framework**: HealthKit  
**Kind**: method

Stops a long-running query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stop(_ query: HKQuery)
```

## Mentions

- [Executing Observer Queries](executing-observer-queries.md)
- [Reading route data](reading-route-data.md)

#### Discussion

Use this method on long-running queries only. Most queries automatically stop after they have gathered the requested data. Long-running queries continue to operate on a background thread, watching the HealthKit store for updates. You can cancel these queries by using this method.

## Parameters

- `query`: Either an   instance or an   instance.

## See Also

- [func execute(HKQuery)](hkhealthstore/execute(_:).md)
  Starts executing the provided query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/stop(_:))*