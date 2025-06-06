# stride(ofValue:)

**Framework**: Swift  
**Kind**: method

Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.

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
static func stride(ofValue value: borrowing T) -> Int
```

#### Return Value

The stride, in bytes, of the given value’s type.

#### Discussion

This is the same as the number of bytes moved when an `UnsafePointer<T>` instance is incremented. `T` may have a lower minimal alignment that trades runtime performance for space efficiency. The result is always positive.

When you have a type instead of an instance, use the `MemoryLayout<T>.stride` static property instead.

```swift
let x: Int = 100

// Finding the stride of a value's type
let s = MemoryLayout.stride(ofValue: x)
// s == 8

// Finding the stride of a type directly
let t = MemoryLayout<Int>.stride
// t == 8
```

## Parameters

- `value`: A value representative of the type to describe.

## See Also

- [static func size(ofValue: borrowing T) -> Int](memorylayout/size(ofvalue:).md)
  Returns the contiguous memory footprint of the given instance.
- [static func alignment(ofValue: borrowing T) -> Int](memorylayout/alignment(ofvalue:).md)
  Returns the default memory alignment of `T`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/memorylayout/stride(ofvalue:))*