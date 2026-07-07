# UniqueArray

**Framework**: Swift  
**Kind**: struct

A dynamically self-resizing, heap allocated, noncopyable array of potentially noncopyable elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct UniqueArray<Element> where Element : ~Copyable
```

#### Overview

`UniqueArray` instances automatically resize their underlying storage as needed to accommodate newly inserted items, using a geometric growth curve. This lets code using `UniqueArray` avoid having to allocate enough capacity in advance; on the other hand, it makes it difficult to tell when and where such reallocations may happen.

For example, appending an element to a `UniqueArray` has highly variable complexity; often, it runs at a constant cost, but if the operation has to resize storage, then the cost of an individual append suddenly becomes proportional to the size of the whole array.

The geometric growth curve allows the cost of such latency spikes to get amortized across repeated invocations, bringing the average cost back to O(1); but the spikes make this construct less suitable for use cases that expect predictable, consistent performance on every operation.

Implicit growth also makes it more difficult to predict/analyze the amount of memory an algorithm would need. Developers targeting environments with stringent limits on heap allocations may prefer to avoid using dynamically resizing container types as a matter of policy. The type `RigidArray` provides a fixed-capacity array variant that caters specifically for these use cases, trading ease-of-use for more consistent/predictable execution. For copyable elements, the copy-on-write `Array` type is an even more convenient and expressive choice.

## Topics

### Initializers
- [init()](uniquearray/init.md)
  Initializes a new unique array with no elements.
- [init(capacity: Int)](uniquearray/init(capacity:).md)
  Initializes a new unique array with the specified capacity and no elements.
- [init(capacity: Int?, copying: some Sequence<Element>)](uniquearray/init(capacity:copying:)-5tkhn.md)
  Creates a new array with the specified initial capacity, holding a copy of the contents of a given sequence.
- [init(capacity: Int?, copying: Span<Element>)](uniquearray/init(capacity:copying:)-991h4.md)
  Creates a new array with the specified capacity, holding a copy of the contents of the given span.
- [init<E>(capacity: Int, initializingWith: (inout OutputSpan<Element>) throws(E) -> Void) throws(E)](uniquearray/init(capacity:initializingwith:).md)
  Creates a new array with the specified capacity, directly initializing its storage using an output span.
- [init(minimumCapacity: Int)](uniquearray/init(minimumcapacity:).md)
  Initializes a new unique array with the specified capacity and no elements.
- [init(repeating: Element, count: Int)](uniquearray/init(repeating:count:).md)
  Creates a new array containing the specified number of a single, repeated value.
### Instance Properties
- [var capacity: Int](uniquearray/capacity.md)
  The maximum number of elements this array can hold without having to reallocate its storage.
- [var count: Int](uniquearray/count.md)
  The number of elements in this array.
- [var debugDescription: String](uniquearray/debugdescription.md)
- [var description: String](uniquearray/description.md)
- [var endIndex: Int](uniquearray/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument. This is always equal to array’s count.
- [var freeCapacity: Int](uniquearray/freecapacity.md)
  The number of additional elements that can be added to this array without reallocating its storage.
- [var indices: Range<Int>](uniquearray/indices.md)
  The range of indices that are valid for subscripting the array.
- [var isEmpty: Bool](uniquearray/isempty.md)
  A Boolean value indicating whether this array contains no elements.
- [var mutableSpan: MutableSpan<Element>](uniquearray/mutablespan.md)
  A mutable span over the elements of this array, providing direct mutating access.
- [var span: Span<Element>](uniquearray/span.md)
  A span over the elements of this array, providing direct read-only access.
- [var startIndex: Int](uniquearray/startindex.md)
  The position of the first element in a nonempty array. This is always zero.
### Instance Methods
- [func append(consuming Element)](uniquearray/append(_:).md)
  Adds an element to the end of the array.
- [func append<E>(addingCount: Int, initializingWith: (inout OutputSpan<Element>) throws(E) -> Void) throws(E)](uniquearray/append(addingcount:initializingwith:).md)
  Append a given number of items to the end of this array by populating an output span.
- [func append(copying: UnsafeBufferPointer<Element>)](uniquearray/append(copying:)-1qhpn.md)
  Copies the elements of a buffer to the end of this array.
- [func append(copying: Span<Element>)](uniquearray/append(copying:)-3aouw.md)
  Copies the elements of a span to the end of this array.
- [func append(copying: some Sequence<Element>)](uniquearray/append(copying:)-7ntgb.md)
  Copies the elements of a sequence to the end of this array.
- [func append(copying: UnsafeMutableBufferPointer<Element>)](uniquearray/append(copying:)-90c4t.md)
  Copies the elements of a buffer to the end of this array.
- [func append(moving: UnsafeMutableBufferPointer<Element>)](uniquearray/append(moving:)-71oaj.md)
  Moves the elements of a buffer to the end of this array, leaving the buffer uninitialized.
- [func append(moving: inout OutputSpan<Element>)](uniquearray/append(moving:)-9p4vs.md)
  Moves the elements of a output span to the end of this array, leaving the span empty.
- [func clone() -> UniqueArray<Element>](uniquearray/clone.md)
  Copy the contents of this array into a newly allocated unique array instance with just enough capacity to hold all its elements.
- [func clone(capacity: Int) -> UniqueArray<Element>](uniquearray/clone(capacity:).md)
  Copy the contents of this array into a newly allocated unique array instance with the specified capacity.
- [func distance(from: UniqueArray<Element>.Index, to: UniqueArray<Element>.Index) -> Int](uniquearray/distance(from:to:).md)
  Returns the distance between two indices.
- [func edit<E, R>((inout OutputSpan<Element>) throws(E) -> R) throws(E) -> R](uniquearray/edit(_:).md)
  Arbitrarily edit the storage underlying this array by invoking a user-supplied closure with a mutable `OutputSpan` view over it. This method calls its function argument at most once, allowing it to arbitrarily modify the contents of the output span it is given. The argument is free to add, remove or reorder any items; however, it is not allowed to replace the span or change its capacity.
- [func formIndex(inout UniqueArray<Element>.Index, offsetBy: inout Int, limitedBy: UniqueArray<Element>.Index)](uniquearray/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, but no further than the given limiting index.
- [func formIndex(after: inout Int)](uniquearray/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Int)](uniquearray/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](uniquearray/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(after: Int) -> Int](uniquearray/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](uniquearray/index(before:).md)
  Returns the position immediately before the given index.
- [func insert(consuming Element, at: Int)](uniquearray/insert(_:at:).md)
  Inserts a new element into the array at the specified position.
- [func insert<E>(addingCount: Int, at: Int, initializingWith: (inout OutputSpan<Element>) throws(E) -> Void) throws(E)](uniquearray/insert(addingcount:at:initializingwith:).md)
  Inserts a given number of new items into this array at the specified position, using a callback to directly initialize array storage by populating an output span.
- [func insert(copying: Span<Element>, at: Int)](uniquearray/insert(copying:at:)-2g824.md)
  Copies the elements of a span into this array at the specified position.
- [func insert(copying: some Collection<Element>, at: Int)](uniquearray/insert(copying:at:)-4823q.md)
  Copies the elements of a collection into this array at the specified position.
- [func insert(copying: UnsafeMutableBufferPointer<Element>, at: Int)](uniquearray/insert(copying:at:)-6kuy5.md)
  Copies the elements of a fully initialized buffer pointer into this array at the specified position.
- [func insert(copying: UnsafeBufferPointer<Element>, at: Int)](uniquearray/insert(copying:at:)-9wt40.md)
  Copies the elements of a fully initialized buffer pointer into this array at the specified position.
- [func insert(moving: UnsafeMutableBufferPointer<Element>, at: Int)](uniquearray/insert(moving:at:)-4f2qc.md)
  Moves the elements of a fully initialized buffer into this array, starting at the specified position, and leaving the buffer uninitialized.
- [func insert(moving: inout OutputSpan<Element>, at: Int)](uniquearray/insert(moving:at:)-6d5t1.md)
  Moves the elements of an output span into this array, starting at the specified position, and leaving the span empty.
- [func isTriviallyIdentical(to: borrowing UniqueArray<Element>) -> Bool](uniquearray/istriviallyidentical(to:).md)
- [func popLast() -> Element?](uniquearray/poplast.md)
  Removes and returns the last element of the array, if there is one.
- [func remove(at: Int) -> Element](uniquearray/remove(at:).md)
  Removes and returns the element at the specified position.
- [func removeAll()](uniquearray/removeall.md)
  Removes all elements from the array, preserving its allocated capacity.
- [func removeLast() -> Element](uniquearray/removelast.md)
  Removes and returns the last element of the array.
- [func removeLast(Int)](uniquearray/removelast(_:).md)
  Removes and discards the specified number of elements from the end of the array.
- [func removeSubrange(some RangeExpression<Int>)](uniquearray/removesubrange(_:)-6hkdt.md)
  Removes the specified subrange of elements from the array.
- [func removeSubrange(Range<Int>)](uniquearray/removesubrange(_:)-6t21j.md)
  Removes the specified subrange of elements from the array.
- [func replaceSubrange<E>(Range<Int>, addingCount: Int, initializingWith: (inout OutputSpan<Element>) throws(E) -> Void) throws(E)](uniquearray/replacesubrange(_:addingcount:initializingwith:).md)
  Replaces the specified range of elements by a given count of new items, using a callback to directly initialize array storage by populating an output span.
- [func replaceSubrange(Range<Int>, copying: UnsafeBufferPointer<Element>)](uniquearray/replacesubrange(_:copying:)-5cbxf.md)
  Replaces the specified subrange of elements by copying the elements of the given buffer pointer, which must be fully initialized.
- [func replaceSubrange(Range<Int>, copying: Span<Element>)](uniquearray/replacesubrange(_:copying:)-70i0j.md)
  Replaces the specified subrange of elements by copying the elements of the given span.
- [func replaceSubrange(Range<Int>, copying: consuming some Collection<Element>)](uniquearray/replacesubrange(_:copying:)-7599g.md)
  Replaces the specified subrange of elements by copying the elements of the given collection.
- [func replaceSubrange(Range<Int>, copying: UnsafeMutableBufferPointer<Element>)](uniquearray/replacesubrange(_:copying:)-8tpt1.md)
  Replaces the specified subrange of elements by copying the elements of the given buffer pointer, which must be fully initialized.
- [func replaceSubrange(Range<Int>, moving: UnsafeMutableBufferPointer<Element>)](uniquearray/replacesubrange(_:moving:)-4de3f.md)
  Replaces the specified range of elements by moving the elements of a fully initialized buffer into their place. On return, the buffer is left in an uninitialized state.
- [func replaceSubrange(Range<Int>, moving: inout OutputSpan<Element>)](uniquearray/replacesubrange(_:moving:)-6vpdp.md)
  Replaces the specified range of elements by moving the contents of an output span into their place. On return, the span is left empty.
- [func reserveCapacity(Int)](uniquearray/reservecapacity(_:).md)
  Ensure that the array has capacity to store the specified number of elements, by growing its storage buffer if necessary.
- [func setCapacity(Int)](uniquearray/setcapacity(_:).md)
  Grow or shrink the capacity of a unique array instance without discarding its contents.
- [func swapAt(Int, Int)](uniquearray/swapat(_:_:).md)
  Exchanges the values at the specified indices of the array.
### Subscripts
- [subscript(Int) -> Element](uniquearray/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [UniqueArray.Index](uniquearray/index.md)
  A type that represents a position in the array: an integer offset from the start.
### Default Implementations
- [Equatable Implementations](uniquearray/equatable-implementations.md)
- [Hashable Implementations](uniquearray/hashable-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [struct UniqueBox](uniquebox.md)
  A smart pointer type that uniquely owns an instance of `Value` on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray)*