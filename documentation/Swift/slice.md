# Slice

**Framework**: Swift  
**Kind**: struct

A view into a subsequence of elements of another collection.

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
@frozen
struct Slice<Base> where Base : Collection
```

#### Overview

A slice stores a base collection and the start and end indices of the view. It does not copy the elements from the collection into separate storage. Thus, creating a slice has O(1) complexity.

#### Slices Share Indices

Indices of a slice can be used interchangeably with indices of the base collection. An element of a slice is located under the same index in the slice and in the base collection, as long as neither the collection nor the slice has been mutated since the slice was created.

For example, suppose you have an array holding the number of absences from each class during a session.

```swift
var absences = [0, 2, 0, 4, 0, 3, 1, 0]
```

You’re tasked with finding the day with the most absences in the second half of the session. To find the index of the day in question, follow these steps:

1. Create a slice of the `absences` array that holds the second half of the days.
2. Use the `max(by:)` method to determine the index of the day with the most absences.
3. Print the result using the index found in step 2 on the original `absences` array.

Here’s an implementation of those steps:

```swift
let secondHalf = absences.suffix(absences.count / 2)
if let i = secondHalf.indices.max(by: { secondHalf[$0] < secondHalf[$1] }) {
    print("Highest second-half absences: \(absences[i])")
}
// Prints "Highest second-half absences: 3"
```

#### Slices Inherit Semantics

A slice inherits the value or reference semantics of its base collection. That is, if a `Slice` instance is wrapped around a mutable collection that has value semantics, such as an array, mutating the original collection would trigger a copy of that collection, and not affect the base collection stored inside of the slice.

For example, if you update the last element of the `absences` array from `0` to `2`, the `secondHalf` slice is unchanged.

```swift
absences[7] = 2
print(absences)
// Prints "[0, 2, 0, 4, 0, 3, 1, 2]"
print(secondHalf)
// Prints "[0, 3, 1, 0]"
```

Use slices only for transient computation. A slice may hold a reference to the entire storage of a larger collection, not just to the portion it presents, even after the base collection’s lifetime ends. Long-term storage of a slice may therefore prolong the lifetime of elements that are no longer otherwise accessible, which can erroneously appear to be memory leakage.

> **Note**: Using a `Slice` instance with a mutable collection requires that the base collection’s `subscript(_: Index)` setter does not invalidate indices. If mutations need to invalidate indices in your custom collection type, don’t use `Slice` as its subsequence type. Instead, define your own subsequence type that takes your index invalidation requirements into account.

## Topics

### Initializers
- [init(base: Base, bounds: Range<Base.Index>)](slice/init(base:bounds:).md)
  Creates a view into the given collection that allows access to elements within the specified range.
### Instance Properties
- [var base: Base](slice/base.md)
  The underlying collection of the slice.
### Instance Methods
- [func assumingMemoryBound<T>(to: T.Type) -> UnsafeMutableBufferPointer<T>](slice/assumingmemorybound(to:)-5fkwu.md)
  Returns a typed buffer to the memory referenced by this buffer slice, assuming that the memory is already bound to the specified type.
- [func assumingMemoryBound<T>(to: T.Type) -> UnsafeBufferPointer<T>](slice/assumingmemorybound(to:)-7a4sa.md)
  Returns a typed buffer to the memory referenced by this buffer slice, assuming that the memory is already bound to the specified type.
- [func bindMemory<T>(to: T.Type) -> UnsafeBufferPointer<T>](slice/bindmemory(to:)-4ombl.md)
  Binds this buffer slice’s memory to the specified type and returns a typed buffer of the bound memory.
- [func bindMemory<T>(to: T.Type) -> UnsafeMutableBufferPointer<T>](slice/bindmemory(to:)-92fs7.md)
  Binds this buffer slice’s memory to the specified type and returns a typed buffer of the bound memory.
- [func copyBytes<C>(from: C)](slice/copybytes(from:).md)
  Copies from a collection of `UInt8` into this buffer slice’s memory.
- [func deinitialize<Element>() -> UnsafeMutableRawBufferPointer](slice/deinitialize.md)
  Deinitializes every instance in this buffer slice.
- [func deinitializeElement<Element>(at: UnsafeMutableBufferPointer<Element>.Index)](slice/deinitializeelement(at:).md)
  Deinitializes the memory underlying the element at `index`.
- [func initialize<S>(from: S) -> (unwritten: S.Iterator, index: Slice<Base>.Index)](slice/initialize(from:).md)
  Initializes the buffer slice’s memory with the given elements.
- [func initialize<Element>(fromContentsOf: some Collection) -> Slice<Base>.Index](slice/initialize(fromcontentsof:).md)
  Initializes the buffer slice’s memory with with every element of the source.
- [func initialize<Element>(repeating: Element)](slice/initialize(repeating:).md)
  Initializes every element in this buffer slice’s memory to a copy of the given value.
- [func initializeElement<Element>(at: Int, to: Element)](slice/initializeelement(at:to:).md)
  Initializes the element at `index` to the given value.
- [func initializeMemory<S>(as: S.Element.Type, from: S) -> (unwritten: S.Iterator, initialized: UnsafeMutableBufferPointer<S.Element>)](slice/initializememory(as:from:).md)
  Initializes the buffer’s memory with the given elements, binding the initialized memory to the elements’ type.
- [func initializeMemory<C>(as: C.Element.Type, fromContentsOf: C) -> UnsafeMutableBufferPointer<C.Element>](slice/initializememory(as:fromcontentsof:).md)
  Initializes the buffer slice’s memory with every element of the source, binding the initialized memory to the elements’ type.
- [func initializeMemory<T>(as: T.Type, repeating: T) -> UnsafeMutableBufferPointer<T>](slice/initializememory(as:repeating:).md)
  Initializes the memory referenced by this buffer slice with the given value, binds the memory to the value’s type, and returns a typed buffer of the initialized memory.
- [func insert(Base.Element, at: Slice<Base>.Index)](slice/insert(_:at:)-4n5zz.md)
- [func insert<S>(contentsOf: S, at: Slice<Base>.Index)](slice/insert(contentsof:at:)-3z6ts.md)
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](slice/load(frombyteoffset:as:)-3vjps.md)
  Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [func load<T>(fromByteOffset: Int, as: T.Type) -> T](slice/load(frombyteoffset:as:)-45bko.md)
  Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](slice/loadunaligned(frombyteoffset:as:)-6jvd4.md)
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](slice/loadunaligned(frombyteoffset:as:)-6u1jm.md)
  Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](slice/loadunaligned(frombyteoffset:as:)-7jjnt.md)
  Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [func loadUnaligned<T>(fromByteOffset: Int, as: T.Type) -> T](slice/loadunaligned(frombyteoffset:as:)-9gtr0.md)
- [func moveElement<Element>(from: Slice<Base>.Index) -> Element](slice/moveelement(from:).md)
  Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.
- [func moveInitialize<Element>(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> Slice<Base>.Index](slice/moveinitialize(fromcontentsof:)-82ebd.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this buffer slice’s memory initialized.
- [func moveInitialize<Element>(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> Slice<Base>.Index](slice/moveinitialize(fromcontentsof:)-iasq.md)
  Moves every element of an initialized source buffer slice into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this buffer slice’s memory initialized.
- [func moveInitializeMemory<T>(as: T.Type, fromContentsOf: UnsafeMutableBufferPointer<T>) -> UnsafeMutableBufferPointer<T>](slice/moveinitializememory(as:fromcontentsof:)-1jll.md)
  Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this slice’s memory initialized.
- [func moveInitializeMemory<T>(as: T.Type, fromContentsOf: Slice<UnsafeMutableBufferPointer<T>>) -> UnsafeMutableBufferPointer<T>](slice/moveinitializememory(as:fromcontentsof:)-1uz4a.md)
  Moves every element from an initialized source buffer slice into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this slice’s memory initialized.
- [func moveUpdate<Element>(fromContentsOf: UnsafeMutableBufferPointer<Element>) -> Slice<Base>.Index](slice/moveupdate(fromcontentsof:)-5i98g.md)
  Updates this buffer slice’s initialized memory initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.
- [func moveUpdate<Element>(fromContentsOf: Slice<UnsafeMutableBufferPointer<Element>>) -> Slice<Base>.Index](slice/moveupdate(fromcontentsof:)-ou4d.md)
  Updates this buffer slice’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.
- [func remove(at: Slice<Base>.Index) -> Base.Element](slice/remove(at:)-pbti.md)
- [func removeSubrange(Range<Slice<Base>.Index>)](slice/removesubrange(_:)-8hbh1.md)
- [func replaceSubrange<C>(Range<Slice<Base>.Index>, with: C)](slice/replacesubrange(_:with:)-904p8.md)
- [func storeBytes<T>(of: T, toByteOffset: Int, as: T.Type)](slice/storebytes(of:tobyteoffset:as:).md)
  Stores a value’s bytes into the buffer pointer slice’s raw memory at the specified byte offset.
- [func update<S>(from: S) -> (unwritten: S.Iterator, index: Slice<Base>.Index)](slice/update(from:).md)
  Updates the buffer slice’s initialized memory with the given elements.
- [func update<Element>(fromContentsOf: some Collection) -> Slice<Base>.Index](slice/update(fromcontentsof:).md)
  Updates the buffer slice’s initialized memory with every element of the source.
- [func update<Element>(repeating: Element)](slice/update(repeating:).md)
  Updates every element of this buffer slice’s initialized memory.
- [func withContiguousMutableStorageIfAvailable<R, Element>((inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R?](slice/withcontiguousmutablestorageifavailable(_:)-2ader.md)
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](slice/withmemoryrebound(to:_:)-1nqta.md)
  Executes the given closure while temporarily binding the buffer slice to instances of type `T`.
- [func withMemoryRebound<T, E, Result>(to: T.Type, (UnsafeMutableBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](slice/withmemoryrebound(to:_:)-3oirt.md)
  Executes the given closure while temporarily binding the buffer slice to instances of type `T`.
- [func withMemoryRebound<T, E, Result, Element>(to: T.Type, (UnsafeMutableBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](slice/withmemoryrebound(to:_:)-6kxii.md)
  Executes the given closure while temporarily binding the memory referenced by this buffer slice to the given type.
- [func withMemoryRebound<T, E, Result, Element>(to: T.Type, (UnsafeBufferPointer<T>) throws(E) -> Result) throws(E) -> Result](slice/withmemoryrebound(to:_:)-ibp7.md)
  Executes the given closure while temporarily binding the memory referenced by this buffer slice to the given type.
### Default Implementations
- [BidirectionalCollection Implementations](slice/bidirectionalcollection-implementations.md)
- [Collection Implementations](slice/collection-implementations.md)
- [LazySequenceProtocol Implementations](slice/lazysequenceprotocol-implementations.md)
- [MutableCollection Implementations](slice/mutablecollection-implementations.md)
- [RangeReplaceableCollection Implementations](slice/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](slice/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/AccelerateBuffer.md)
- [AccelerateMutableBuffer](../Accelerate/AccelerateMutableBuffer.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [MutableCollection](mutablecollection.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice)*