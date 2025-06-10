# Collections

**Framework**: Swift

Store and organize data using arrays, dictionaries, sets, and other data structures.

## Topics

### Arrays and Dictionaries
- [struct Array](array.md)
  An ordered, random-access collection.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.
- [struct InlineArray](inlinearray.md)
  A fixed-size array.
### Sets
- [struct Set](set.md)
  An unordered collection of unique elements.
- [protocol OptionSet](optionset.md)
  A type that presents a mathematical set interface to a bit set.
### Ranges
- [static func ..< (Self, Self) -> Range<Self>](comparable/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [struct Range](range.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.
- [struct RangeSet](rangeset.md)
  A set of values of any comparable type, represented by ranges.
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [struct ClosedRange](closedrange.md)
  An interval from a lower bound up to, and including, an upper bound.
### Strides
- [func stride<T>(from: T, to: T, by: T.Stride) -> StrideTo<T>](stride(from:to:by:).md)
  Returns a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [func stride<T>(from: T, through: T, by: T.Stride) -> StrideThrough<T>](stride(from:through:by:).md)
  Returns a sequence from a starting value toward, and possibly including, an end value, stepping by the specified amount.
### Special-Use Collections
- [func repeatElement<T>(T, count: Int) -> Repeated<T>](repeatelement(_:count:).md)
  Creates a collection containing the specified number of the given element.
- [struct CollectionOfOne](collectionofone.md)
  A collection containing a single element.
- [struct EmptyCollection](emptycollection.md)
  A collection whose element type is `Element` but that is always empty.
- [struct KeyValuePairs](keyvaluepairs.md)
  A lightweight collection of key-value pairs.
- [typealias DictionaryLiteral](dictionaryliteral.md)
### Dynamic Sequences
- [func sequence<T>(first: T, next: (T) -> T?) -> UnfoldFirstSequence<T>](sequence(first:next:).md)
  Returns a sequence formed from `first` and repeated lazy applications of `next`.
- [func sequence<T, State>(state: State, next: (inout State) -> T?) -> UnfoldSequence<T, State>](sequence(state:next:).md)
  Returns a sequence formed from repeated lazy applications of `next` to a mutable `state`.
### Joint Iteration
- [func zip<Sequence1, Sequence2>(Sequence1, Sequence2) -> Zip2Sequence<Sequence1, Sequence2>](zip(_:_:).md)
  Creates a sequence of pairs built out of two underlying sequences.
### Advanced Collection Topics
- [Sequence and Collection Protocols](sequence-and-collection-protocols.md)
  Write generic code that works with any collection, or build your own collection types.
- [Supporting Types](supporting-types.md)
  Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.
- [Managed Buffers](managed-buffers.md)
  Build your own buffer-backed collection types.

## See Also

- [Numbers and Basic Values](numbers-and-basic-values.md)
  Model data with numbers, Boolean values, and other fundamental types.
- [Strings and Text](strings-and-text.md)
  Work with text using Unicode-safe strings.
- [Time](time-and-duration.md)
  Measure how long an operation takes and determine schedules in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collections)*