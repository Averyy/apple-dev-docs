---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# Dictionary

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: extension  
**Role**: Extended Structure

## Declaration

```swift
extension Dictionary
```

## Topics

### Initializers
- [init<S>(S, uniquingKeysWith: (Value, Value) async throws -> Value) async rethrows](./dictionary/init%28_,uniquingkeyswith%29.md)
  Creates a new dictionary from the key-value pairs in the given asynchronous sequence, using a combining closure to determine the value for any duplicate keys.
- [init<S>(grouping: S, by: (S.Element) async throws -> Key) async rethrows](./dictionary/init%28grouping,by%29.md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.
- [init<S>(uniqueKeysWithValues: S) async rethrows](./dictionary/init%28uniquekeyswithvalues%29.md)
  Creates a new dictionary from the key-value pairs in the given asynchronous sequence.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary)*