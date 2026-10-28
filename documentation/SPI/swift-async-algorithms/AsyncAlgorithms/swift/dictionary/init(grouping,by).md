---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(grouping:by:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# init(grouping:by:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: init  
**Role**: Initializer

Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
init<S>(grouping values: S, by keyForValue: (S.Element) async throws -> Key) async rethrows where Value == [S.Element], S : AsyncSequence
```

Available when `Key` conforms to `Hashable`.

## Discussion

The arrays in the “values” position of the new dictionary each contain at least one element, with the elements in the same order as the source asynchronous sequence.

## Parameters

- `values`: An asynchronous sequence of values to group into a dictionary.
- `keyForValue`: A closure that returns a key for each element in `values`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(grouping:by:))*