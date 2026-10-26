---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/merge(_:_:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# merge(_:_:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: func  
**Role**: Function

Creates an asynchronous sequence of elements from two underlying asynchronous sequences

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func merge<Base1, Base2, Base3>(_ base1: Base1, _ base2: Base2, _ base3: Base3) -> AsyncMerge3Sequence<Base1, Base2, Base3> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base3 : Sendable, Base3 : AsyncSequence, Base1.Element : Sendable, Base1.Element == Base2.Element, Base2.Element == Base3.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/merge(_:_:_:))*