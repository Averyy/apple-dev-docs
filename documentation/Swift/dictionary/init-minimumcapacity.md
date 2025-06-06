# init(minimumCapacity:)

**Framework**: Swift  
**Kind**: init

Creates an empty dictionary with preallocated space for at least the specified number of elements.

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
init(minimumCapacity: Int)
```

#### Discussion

Use this initializer to avoid intermediate reallocations of a dictionary’s storage buffer when you know how many key-value pairs you are adding to a dictionary after creation.

## Parameters

- `minimumCapacity`: The minimum number of key-value pairs that   the newly created dictionary should be able to store without   reallocating its storage buffer.

## See Also

- [init()](dictionary/init.md)
  Creates an empty dictionary.
- [init<S>(uniqueKeysWithValues: S)](dictionary/init(uniquekeyswithvalues:).md)
  Creates a new dictionary from the key-value pairs in the given sequence.
- [init<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/init(_:uniquingkeyswith:).md)
  Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init<S>(grouping: S, by: (S.Element) throws -> Key) rethrows](dictionary/init(grouping:by:).md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init(minimumcapacity:))*