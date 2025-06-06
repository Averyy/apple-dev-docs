# result(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query that asynchronously reads matching clinical records.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> [HKVerifiableClinicalRecord]
```

## Parameters

- `healthStore`: The access point for HealthKit data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquerydescriptor/result(for:))*