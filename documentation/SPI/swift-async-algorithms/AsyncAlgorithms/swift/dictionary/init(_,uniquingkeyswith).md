---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(_:uniquingkeyswith:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# init(_:uniquingKeysWith:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: init  
**Role**: Initializer

Creates a new dictionary from the key-value pairs in the given asynchronous sequence, using a combining closure to determine the value for any duplicate keys.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
init<S>(_ keysAndValues: S, uniquingKeysWith combine: (Value, Value) async throws -> Value) async rethrows where S : AsyncSequence, S.Element == (Key, Value)
```

Available when `Key` conforms to `Hashable`.

## Discussion

You use this initializer to create a dictionary when you have a sequence of key-value tuples that might have duplicate keys. As the dictionary is built, the initializer calls the `combine` closure with the current and new values for any duplicate keys. Pass a closure as `combine` that returns the value to use in the resulting dictionary: The closure can choose between the two values, combine them to produce a new value, or even throw an error.

## Parameters

- `keysAndValues`: An asynchronous sequence of key-value pairs to use for the new dictionary.
- `combine`: A closure that is called with the values for any duplicate keys that are encountered. The closure returns the desired value for the final dictionary, or throws an error if building the dictionary can’t proceed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/swift/dictionary/init(_:uniquingkeyswith:))*