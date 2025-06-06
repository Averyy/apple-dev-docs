# isEmpty

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the dictionary is empty.

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
var isEmpty: Bool { get }
```

#### Discussion

Dictionaries are empty when created with an initializer or an empty dictionary literal.

```swift
var frequencies: [String: Int] = [:]
print(frequencies.isEmpty)
// Prints "true"
```

## See Also

- [var count: Int](dictionary/count.md)
  The number of key-value pairs in the dictionary.
- [var capacity: Int](dictionary/capacity.md)
  The total number of key-value pairs that the dictionary can contain without allocating new storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/isempty)*