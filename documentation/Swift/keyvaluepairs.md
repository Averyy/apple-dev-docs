# KeyValuePairs

**Framework**: Swift  
**Kind**: struct

A lightweight collection of key-value pairs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct KeyValuePairs<Key, Value>
```

#### Overview

Use a `KeyValuePairs` instance when you need an ordered collection of key-value pairs and don’t require the fast key lookup that the `Dictionary` type provides. Unlike key-value pairs in a true dictionary, neither the key nor the value of a `KeyValuePairs` instance must conform to the `Hashable` protocol.

You initialize a `KeyValuePairs` instance using a Swift dictionary literal. Besides maintaining the order of the original dictionary literal, `KeyValuePairs` also allows duplicates keys. For example:

```swift
let recordTimes: KeyValuePairs = ["Florence Griffith-Joyner": 10.49,
                                      "Evelyn Ashford": 10.76,
                                      "Evelyn Ashford": 10.79,
                                      "Marlies Gohr": 10.81]
print(recordTimes.first!)
// Prints "(key: "Florence Griffith-Joyner", value: 10.49)"
```

Some operations that are efficient on a dictionary are slower when using `KeyValuePairs`. In particular, to find the value matching a key, you must search through every element of the collection. The call to `firstIndex(where:)` in the following example must traverse the whole collection to find the element that matches the predicate:

```swift
let runner = "Marlies Gohr"
if let index = recordTimes.firstIndex(where: { $0.0 == runner }) {
    let time = recordTimes[index].1
    print("\(runner) set a 100m record of \(time) seconds.")
} else {
    print("\(runner) couldn't be found in the records.")
}
// Prints "Marlies Gohr set a 100m record of 10.81 seconds."
```

#### Key Value Pairs As a Function Parameter

When calling a function with a `KeyValuePairs` parameter, you can pass a Swift dictionary literal without causing a `Dictionary` to be created. This capability can be especially important when the order of elements in the literal is significant.

For example, you could create an `IntPairs` structure that holds a list of two-integer tuples and use an initializer that accepts a `KeyValuePairs` instance.

```swift
struct IntPairs {
    var elements: [(Int, Int)]

    init(_ elements: KeyValuePairs<Int, Int>) {
        self.elements = Array(elements)
    }
}
```

When you’re ready to create a new `IntPairs` instance, use a dictionary literal as the parameter to the `IntPairs` initializer. The `KeyValuePairs` instance preserves the order of the elements as passed.

```swift
let pairs = IntPairs([1: 2, 1: 1, 3: 4, 2: 1])
print(pairs.elements)
// Prints "[(1, 2), (1, 1), (3, 4), (2, 1)]"
```

## Topics

### Initializers
- [init(dictionaryLiteral: (Key, Value)...)](keyvaluepairs/init(dictionaryliteral:).md)
  Creates a new `KeyValuePairs` instance from the given dictionary literal.
### Instance Properties
- [var span: Span<KeyValuePairs<Key, Value>.Element>](keyvaluepairs/span.md)
### Default Implementations
- [BidirectionalCollection Implementations](keyvaluepairs/bidirectionalcollection-implementations.md)
- [Collection Implementations](keyvaluepairs/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](keyvaluepairs/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](keyvaluepairs/customstringconvertible-implementations.md)
- [RandomAccessCollection Implementations](keyvaluepairs/randomaccesscollection-implementations.md)
- [Sequence Implementations](keyvaluepairs/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomStringConvertible](customstringconvertible.md)
- [ExpressibleByDictionaryLiteral](expressiblebydictionaryliteral.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [func repeatElement<T>(T, count: Int) -> Repeated<T>](repeatelement(_:count:).md)
  Creates a collection containing the specified number of the given element.
- [struct CollectionOfOne](collectionofone.md)
  A collection containing a single element.
- [struct EmptyCollection](emptycollection.md)
  A collection whose element type is `Element` but that is always empty.
- [typealias DictionaryLiteral](dictionaryliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs)*