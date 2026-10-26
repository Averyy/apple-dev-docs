---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/zip(_:_:_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# zip(_:_:_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: func  
**Role**: Function

Creates an asynchronous sequence that concurrently awaits values from three `AsyncSequence` types and emits a tuple of the values.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func zip<Base1, Base2, Base3>(_ base1: Base1, _ base2: Base2, _ base3: Base3) -> AsyncZip3Sequence<Base1, Base2, Base3> where Base1 : Sendable, Base1 : AsyncSequence, Base2 : Sendable, Base2 : AsyncSequence, Base3 : Sendable, Base3 : AsyncSequence, Base1.Element : Sendable, Base2.Element : Sendable, Base3.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/zip(_:_:_:))*