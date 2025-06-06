# HKSourceQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKSourceQueryDescriptor<Sample> where Sample : HKSample
```

## Mentions

- [Reading data from HealthKit](reading-data-from-healthkit.md)

#### Overview

Use [`HKSourceQueryDescriptor`](hksourcequerydescriptor.md) to run a general query that returns a snapshot of all the apps and devices that have saved matching data to the HealthKit store.

```swift
// Create the source descriptor.
let sourceDescriptor = HKSourceQueryDescriptor(predicate: .workout())

// Read the source data from the HealthKit store.
let sources = try await sourceDescriptor.result(for: store)

for source in sources {
    // Process the sources here.
    print(source)
}
```

When you call the descriptor’s [`result(for:)`](hksourcequerydescriptor/result(for:).md) method, it creates and executes an [`HKSourceQuery`](hksourcequery.md) in the background, passing the results as an array of [`HKSource`](hksource.md) instances.

## Topics

### Creating Source Query Descriptors
- [init(predicate: HKSamplePredicate<Sample>)](hksourcequerydescriptor/init(predicate:).md)
  Creates a source query descriptor.
### Running Queries
- [func result(for: HKHealthStore) async throws -> [HKSource]](hksourcequerydescriptor/result(for:).md)
  Runs a one-shot query that asynchronously returns a snapshot of all the sources that saved matching data.
### Accessing Query Properties
- [var predicate: HKSamplePredicate<Sample>](hksourcequerydescriptor/predicate.md)
  A predicate that limits the data used by the query.
### Default Implementations
- [HKAsyncQuery Implementations](hksourcequerydescriptor/hkasyncquery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncQuery](hkasyncquery.md)

## See Also

- [class HKSourceRevision](hksourcerevision.md)
  An object indicating the source of a HealthKit sample.
- [class HKSource](hksource.md)
  An object indicating the app or device that created a HealthKit sample
- [class HKDevice](hkdevice.md)
  A device that generates data for HealthKit.
- [class HKSourceQuery](hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcequerydescriptor)*