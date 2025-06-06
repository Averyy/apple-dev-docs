# filter(matchingCategory:)

**Framework**: RealityKit  
**Kind**: method

Filters a sequence of tags based on matching the specified category.  Returns the tags that match the specified category.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func filter<T>(matchingCategory category: CMTypedTag<T>.Category) -> [CMTypedTag<T>] where T : Sendable
```

#### Discussion

- category: The category to match.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](queryresult/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](queryresult/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/queryresult/filter(matchingcategory:))*