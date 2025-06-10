# LazyDropWhileCollection

**Framework**: Swift  
**Kind**: typealias

A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.

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
typealias LazyDropWhileCollection<T> = LazyDropWhileSequence<T> where T : Collection
```

#### Discussion

> **Note**: The performance of accessing `startIndex`, `first`, or any methods that depend on `startIndex` depends on how many elements satisfy the predicate at the start of the collection, and may not offer the usual performance given by the `Collection` protocol. Be aware, therefore, that general operations on lazy collections may not have the documented complexity.

## See Also

- [struct LazySequence](lazysequence.md)
  A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [struct LazyMapSequence](lazymapsequence.md)
  A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [struct LazyFilterSequence](lazyfiltersequence.md)
  A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [struct LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
  A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [struct LazyDropWhileSequence](lazydropwhilesequence.md)
  A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [typealias LazyCollection](lazycollection.md)
  A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [typealias LazyFilterCollection](lazyfiltercollection.md)
  A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [typealias LazyMapCollection](lazymapcollection.md)
  A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [typealias LazyPrefixWhileCollection](lazyprefixwhilecollection.md)
  A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazydropwhilecollection)*