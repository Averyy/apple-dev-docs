# popFirst()

**Framework**: Swift  
**Kind**: method

Removes and returns the first key-value pair of the dictionary if the dictionary isn’t empty.

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
mutating func popFirst() -> Dictionary<Key, Value>.Element?
```

#### Return Value

The first key-value pair of the dictionary if the dictionary is not empty; otherwise, `nil`.

#### Discussion

The first element of the dictionary is not necessarily the first element added. Don’t expect any particular ordering of key-value pairs.

> **Note**: Averages to O(1) over many calls to `popFirst()`.

Averages to O(1) over many calls to `popFirst()`.

## See Also

- [func dropFirst(Int) -> Self.SubSequence](dictionary/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dictionary/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropLast(Int) -> Self.SubSequence](dictionary/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/popfirst())*