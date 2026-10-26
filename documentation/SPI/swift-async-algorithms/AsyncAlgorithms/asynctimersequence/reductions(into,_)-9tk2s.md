---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/reductions(into:_:)-9tk2s"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# reductions(into:_:)

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
func reductions<Result>(into initial: Result, _ transform: @escaping @Sendable (inout Result, Self.Element) async -> Void) -> AsyncExclusiveReductionsSequence<Self, Result>
```

#### Return Value

An asynchronous sequence of the reduced elements.

#### Discussion

Starting from the initial value, this combines each element of the base asynchronous sequence with the running result and emits each intermediate result. The initial value itself is not emitted, so the first element of the returned sequence is the result of combining the initial value with the first element of the base sequence. If the base sequence is empty, the returned sequence is also empty.

## Parameters

- `initial`: The value to use as the initial value.
- `transform`: A closure that combines the previously-reduced result and the next element in the receiving asynchronous sequence, mutating the previous result instead of returning a value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynctimersequence/reductions(into:_:)-9tk2s)*