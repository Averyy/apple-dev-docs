# MemoryLayout

**Framework**: Swift  
**Kind**: enum

The memory layout of a type, describing its size, stride, and alignment.

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
enum MemoryLayout<T> where T : ~Copyable, T : ~Escapable
```

#### Overview

You can use `MemoryLayout` as a source of information about a type when allocating or binding memory using raw pointers. The following example declares a `Point` type with `x` and `y` coordinates and a Boolean `isFilled` property.

```swift
struct Point {
    let x: Double
    let y: Double
    let isFilled: Bool
}
```

The size, stride, and alignment of the `Point` type are accessible as static properties of `MemoryLayout<Point>`.

```swift
// MemoryLayout<Point>.size == 17
// MemoryLayout<Point>.stride == 24
// MemoryLayout<Point>.alignment == 8
```

Always use a multiple of a type’s `stride` instead of its `size` when allocating memory or accounting for the distance between instances in memory. This example allocates uninitialized raw memory with space for four instances of `Point`.

```swift
let count = 4
let pointPointer = UnsafeMutableRawPointer.allocate(
        byteCount: count * MemoryLayout<Point>.stride,
        alignment: MemoryLayout<Point>.alignment)
```

## Topics

### Accessing the Layout of a Type
- [static var size: Int](memorylayout/size.md)
  The contiguous memory footprint of `T`, in bytes.
- [static var alignment: Int](memorylayout/alignment.md)
  The default memory alignment of `T`, in bytes.
- [static var stride: Int](memorylayout/stride.md)
  The number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
### Accessing the Layout of a Value
- [static func stride(ofValue: borrowing T) -> Int](memorylayout/stride(ofvalue:).md)
  Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [static func size(ofValue: borrowing T) -> Int](memorylayout/size(ofvalue:).md)
  Returns the contiguous memory footprint of the given instance.
- [static func alignment(ofValue: borrowing T) -> Int](memorylayout/alignment(ofvalue:).md)
  Returns the default memory alignment of `T`.
### Querying Type Properties
- [static func offset(of: PartialKeyPath<T>) -> Int?](memorylayout/offset(of:).md)
  Returns the offset of an inline stored property within a type’s in-memory representation.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/memorylayout)*