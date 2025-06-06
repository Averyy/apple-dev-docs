# result(for:)

**Framework**: HealthKit  
**Kind**: method  
**Required**: Yes

Runs a one-shot query and asynchronously returns a snapshot of the current matching results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> Self.Output
```

## Mentions

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)

#### Discussion

The adopting type’s [`Output`](hkasyncquery/output.md) associated type specifies the values that this method returns. For example, [`HKSampleQueryDescriptor`](hksamplequerydescriptor.md) returns an array of [`HKQuantitySample`](hkquantitysample.md) objects.

```swift
let stepType = HKQuantityType(.stepCount)

let descriptor = HKSampleQueryDescriptor(
    predicates:[.quantitySample(type: stepType)],
    sortDescriptors: [SortDescriptor(\.endDate, order: .reverse)],
    limit: 10)

let results = try await descriptor.result(for: store)
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [associatedtype Output](hkasyncquery/output.md)
  The type of data that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkasyncquery/result(for:))*