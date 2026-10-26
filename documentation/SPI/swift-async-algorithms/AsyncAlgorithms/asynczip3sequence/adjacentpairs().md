---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip3sequence/adjacentpairs()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# adjacentPairs()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

An `AsyncSequence` that iterates over the adjacent pairs of the original original `AsyncSequence`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func adjacentPairs() -> AsyncAdjacentPairsSequence<Self>
```

#### Return Value

An `AsyncSequence` where the element is a tuple of two adjacent elements or the original `AsyncSequence`.

#### Discussion

```
for await (first, second) in (1...5).async.adjacentPairs() {
   print("First: \(first), Second: \(second)")
}

// First: 1, Second: 2
// First: 2, Second: 3
// First: 3, Second: 4
// First: 4, Second: 5
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asynczip3sequence/adjacentpairs())*