---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence/reductions(_:)-4efsu"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# reductions(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given error-throwing closure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reductions(_ transform: @escaping @Sendable (Self.Element, Self.Element) async throws -> Self.Element) -> AsyncThrowingInclusiveReductionsSequence<Self>
```

## Return Value

An asynchronous sequence of the reduced elements.

## Discussion

This can be seen as applying the reduce function to each element and providing the initial value followed by these results as an asynchronous sequence.

```
let runningTotal = [1, 2, 3, 4].async.reductions(+)
print(await Array(runningTotal))

// prints [1, 3, 6, 10]
```

## Parameters

- `transform`: A closure that combines the previously reduced result and the next element in the receiving sequence. If the closure throws an error, the sequence throws.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/_concurrency/asyncsequence/reductions(_:)-4efsu)*