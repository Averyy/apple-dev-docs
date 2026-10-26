---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/chain(_:_:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# chain(_:_:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: func  
**Role**: Function

Returns a new asynchronous sequence that iterates over the three given asynchronous sequences, one followed by the other.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func chain<Base1, Base2, Base3>(_ s1: Base1, _ s2: Base2, _ s3: Base3) -> AsyncChain3Sequence<Base1, Base2, Base3> where Base1 : AsyncSequence, Base2 : AsyncSequence, Base3 : AsyncSequence, Base1.Element == Base2.Element, Base2.Element == Base3.Element
```

#### Return Value

An asynchronous sequence that iterates first over the elements of `s1`, and then over the elements of `s2`, and then over the elements of `s3`

## Parameters

- `s1`: The first asynchronous sequence.
- `s2`: The second asynchronous sequence.
- `s3`: The third asynchronous sequence.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/chain(_:_:_:))*