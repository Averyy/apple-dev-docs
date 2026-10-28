---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/combinelatest(_:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# combineLatest(_:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: func  
**Role**: Function

Creates an asynchronous sequence that combines the latest values from two `AsyncSequence` types by emitting a tuple of the values. [`combineLatest(_:_:)`](./combinelatest%28_,_%29.md) only emits a value whenever any of the base `AsyncSequence`s emit a value (so long as each of the bases have emitted at least one value).

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func combineLatest<Base1, Base2>(_ base1: Base1, _ base2: Base2) -> AsyncCombineLatest2Sequence<Base1, Base2> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable
```

## Discussion

Finishes: [`combineLatest(_:_:)`](./combinelatest%28_,_%29.md) finishes when one of the bases finishes before emitting any value or when all bases finished.

Throws: [`combineLatest(_:_:)`](./combinelatest%28_,_%29.md) throws when one of the bases throws. If one of the bases threw any buffered and not yet consumed values will be dropped.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/combinelatest(_:_:))*