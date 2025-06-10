# ContiguousArray

**Framework**: Swift  
**Kind**: struct

A contiguously stored array.

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
struct ContiguousArray<Element>
```

#### Overview

The `ContiguousArray` type is a specialized array that always stores its elements in a contiguous region of memory. This contrasts with `Array`, which can store its elements in either a contiguous region of memory or an `NSArray` instance if its `Element` type is a class or `@objc` protocol.

If your array’s `Element` type is a class or `@objc` protocol and you do not need to bridge the array to `NSArray` or pass the array to Objective-C APIs, using `ContiguousArray` may be more efficient and have more predictable performance than `Array`. If the array’s `Element` type is a struct or enumeration, `Array` and `ContiguousArray` should have similar efficiency.

For more information about using arrays, see `Array` and `ArraySlice`, with which `ContiguousArray` shares most properties and methods.

## Topics

### Initializers
- [init<S>(S)](contiguousarray/init(_:).md)
  Creates an array containing the elements of a sequence.
- [init(unsafeUninitializedCapacity: Int, initializingWith: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws -> Void) rethrows](contiguousarray/init(unsafeuninitializedcapacity:initializingwith:).md)
  Creates an array with the specified capacity, then calls the given closure with a buffer covering the array’s uninitialized memory.
### Instance Properties
- [var capacity: Int](contiguousarray/capacity.md)
  The total number of elements that the array can contain without allocating new storage.
- [var mutableSpan: MutableSpan<Element>](contiguousarray/mutablespan.md)
- [var span: Span<Element>](contiguousarray/span.md)
### Instance Methods
- [func insert(Element, at: Int)](contiguousarray/insert(_:at:).md)
  Inserts a new element at the specified position.
- [func remove(at: Int) -> Element](contiguousarray/remove(at:).md)
  Removes and returns the element at the specified position.
- [func reserveCapacity(Int)](contiguousarray/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.
- [func withUnsafeBufferPointer<R, E>((UnsafeBufferPointer<Element>) throws(E) -> R) throws(E) -> R](contiguousarray/withunsafebufferpointer(_:).md)
  Calls a closure with a pointer to the array’s contiguous storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](contiguousarray/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [func withUnsafeMutableBufferPointer<R, E>((inout UnsafeMutableBufferPointer<Element>) throws(E) -> R) throws(E) -> R](contiguousarray/withunsafemutablebufferpointer(_:).md)
  Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer) throws -> R) rethrows -> R](contiguousarray/withunsafemutablebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.
### Default Implementations
- [Attachable Implementations](contiguousarray/attachable-implementations.md)
- [BidirectionalCollection Implementations](contiguousarray/bidirectionalcollection-implementations.md)
- [Collection Implementations](contiguousarray/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](contiguousarray/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](contiguousarray/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](contiguousarray/customstringconvertible-implementations.md)
- [Decodable Implementations](contiguousarray/decodable-implementations.md)
- [Encodable Implementations](contiguousarray/encodable-implementations.md)
- [Equatable Implementations](contiguousarray/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](contiguousarray/expressiblebyarrayliteral-implementations.md)
- [Hashable Implementations](contiguousarray/hashable-implementations.md)
- [MutableCollection Implementations](contiguousarray/mutablecollection-implementations.md)
- [OperationParameter Implementations](contiguousarray/operationparameter-implementations.md)
- [RandomAccessCollection Implementations](contiguousarray/randomaccesscollection-implementations.md)
- [RangeReplaceableCollection Implementations](contiguousarray/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](contiguousarray/sequence-implementations.md)

## Relationships

### Conforms To
- [AccelerateBuffer](../Accelerate/AccelerateBuffer.md)
- [AccelerateMutableBuffer](../Accelerate/AccelerateMutableBuffer.md)
- [Attachable](../Testing/Attachable.md)
- [BNNSGraph.Builder.OperationParameter](../Accelerate/BNNSGraph/Builder/OperationParameter.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
- [Hashable](hashable.md)
- [MutableCollection](mutablecollection.md)
- [MutableDataProtocol](../Foundation/MutableDataProtocol.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [struct ArraySlice](arrayslice.md)
  A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray)*