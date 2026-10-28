---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(uniquekeyswithvalues:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# init(uniqueKeysWithValues:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: init  
**Role**: Initializer

Creates a new dictionary from the key-value pairs in the given asynchronous sequence.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
init<S>(uniqueKeysWithValues keysAndValues: S) async rethrows where S : AsyncSequence, S.Element == (Key, Value)
```

Available when `Key` conforms to `Hashable`.

## Discussion

You use this initializer to create a dictionary when you have an asynchronous sequence of key-value tuples with unique keys. Passing an asynchronous sequence with duplicate keys to this initializer results in a runtime error. If your asynchronous sequence might have duplicate keys, use the `Dictionary(_:uniquingKeysWith:)` initializer instead.

> **Precondition**: The sequence must not have duplicate keys.

## Parameters

- `keysAndValues`: An asynchronous sequence of key-value pairs to use for the new dictionary. Every key in `keysAndValues` must be unique.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(uniquekeyswithvalues:))*