# InlineArray

**Framework**: Swift  
**Kind**: struct

A fixed-size array.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct InlineArray<let count : Int, Element> where Element : ~Copyable
```

#### Overview

The `InlineArray` type is a specialized array that stores its elements contiguously inline, rather than allocating an out-of-line region of memory with copy-on-write optimization.

#### Memory Layout

An  array’s size is zero. Its stride and alignment are one byte.

A  array’s size and stride are equal to the element’s stride multiplied by the number of elements. Its alignment is equal to the element’s alignment.

```swift
MemoryLayout<InlineArray<3, UInt16>>.size       //-> 6
MemoryLayout<InlineArray<3, UInt16>>.stride     //-> 6
MemoryLayout<InlineArray<3, UInt16>>.alignment  //-> 2
```

#### Literal Initialization

Array literal syntax can be used to initialize an `InlineArray` instance. A stack-allocated array will do in-place initialization of each element. The `count` and/or `Element` can be inferred from the array literal.

```swift
let a: InlineArray<4, Int> = [1, 2, 4, 8]
let b: InlineArray<_, Int> = [1, 2, 4, 8]
let c: InlineArray<4, _>   = [1, 2, 4, 8]
let d: InlineArray         = [1, 2, 4, 8]
```

## Topics

### Initializers
- [init<E>((InlineArray<count, Element>.Index) throws(E) -> Element) throws(E)](inlinearray/init(_:).md)
  Initializes every element in this array, by calling the given closure with each index.
- [init<E>(first: consuming Element, next: (borrowing Element) throws(E) -> Element) throws(E)](inlinearray/init(first:next:).md)
  Initializes every element in this array, by calling the given closure with each preceding element.
- [init(repeating: Element)](inlinearray/init(repeating:).md)
  Initializes every element in this array to a copy of the given value.
### Instance Properties
- [var count: Int](inlinearray/count.md)
  The number of elements in the array.
- [var endIndex: InlineArray<count, Element>.Index](inlinearray/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<InlineArray<count, Element>.Index>](inlinearray/indices.md)
  The indices that are valid for subscripting the array, in ascending order.
- [var isEmpty: Bool](inlinearray/isempty.md)
  A Boolean value indicating whether the array is empty.
- [var mutableSpan: MutableSpan<Element>](inlinearray/mutablespan.md)
- [var span: Span<Element>](inlinearray/span.md)
- [var startIndex: InlineArray<count, Element>.Index](inlinearray/startindex.md)
  The position of the first element in a nonempty array.
### Instance Methods
- [func index(after: InlineArray<count, Element>.Index) -> InlineArray<count, Element>.Index](inlinearray/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: InlineArray<count, Element>.Index) -> InlineArray<count, Element>.Index](inlinearray/index(before:).md)
  Returns the position immediately before the given index.
- [func swapAt(InlineArray<count, Element>.Index, InlineArray<count, Element>.Index)](inlinearray/swapat(_:_:).md)
  Exchanges the values at the specified indices of the array.
### Subscripts
- [subscript(InlineArray<count, Element>.Index) -> Element](inlinearray/subscript(_:).md)
  Accesses the element at the specified position.
- [subscript(unchecked _: InlineArray<count, Element>.Index) -> Element](inlinearray/subscript(unchecked:).md)
  Accesses the element at the specified position.
### Type Aliases
- [InlineArray.Element](inlinearray/element.md)
  The type of the array’s elements.
- [InlineArray.Index](inlinearray/index.md)
  A type that represents a position in the array.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct Array](array.md)
  An ordered, random-access collection.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray)*