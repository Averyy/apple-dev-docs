# popFirst()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes and returns the first element of the set.

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
mutating func popFirst() -> Element?
```

Available when `Element` conforms to `Hashable`.

#### Return Value

A member of the set. If the set is empty, returns `nil`.

#### Discussion

Because a set is not an ordered collection, the “first” element may not be the first element that was added to the set.

## See Also

### Excluding Elements
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./drop%28while%29.md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](./dropfirst%28_%29.md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/popfirst())*