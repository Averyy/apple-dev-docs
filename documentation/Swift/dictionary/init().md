# init()

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates an empty dictionary.

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
init()
```

## See Also

### Creating a Dictionary
- [init(minimumCapacity: Int)](./init%28minimumcapacity%29.md)
  Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init<S>(uniqueKeysWithValues: S)](./init%28uniquekeyswithvalues%29.md)
  Creates a new dictionary from the key-value pairs in the given sequence.
- [init<S, E>(S, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E)](./init%28_,uniquingkeyswith%29.md)
  Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init<S, E>(grouping: S, by: (S.Element) throws(E) -> Key) throws(E)](./init%28grouping,by%29.md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init())*