---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/reductions(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# reductions(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Returns an asynchronous sequence containing the accumulated results of combining the elements of the asynchronous sequence using the given closure.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func reductions(_ transform: @escaping @Sendable (Self.Element, Self.Element) async -> Self.Element) -> AsyncInclusiveReductionsSequence<Self>
```

## Return Value

An asynchronous sequence of the reduced elements.

## Discussion

This can be seen as applying the reduce function to each element and producing an asynchronous sequence consisting of the initial value followed by these results.

```
let runningTotal = [1, 2, 3, 4].async.reductions(+)
print(await Array(runningTotal))

// prints [1, 3, 6, 10]
```

## Parameters

- `transform`: A closure that combines the previously reduced result and the next element in the receiving sequence, and returns the result.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncexclusivereductionssequence/reductions(_:))*