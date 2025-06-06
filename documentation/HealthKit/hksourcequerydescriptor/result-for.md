# result(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query that asynchronously returns a snapshot of all the sources that saved matching data.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> [HKSource]
```

## Parameters

- `healthStore`: The access point for HealthKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcequerydescriptor/result(for:))*