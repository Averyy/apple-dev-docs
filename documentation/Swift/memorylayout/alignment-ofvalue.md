# alignment(ofValue:)

**Framework**: Swift  
**Kind**: method

Returns the default memory alignment of `T`.

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
static func alignment(ofValue value: borrowing T) -> Int
```

#### Return Value

The default memory alignment, in bytes, of the given value’s type. This value is always positive.

#### Discussion

Use a type’s alignment when allocating memory using an unsafe pointer.

When you have a type instead of an instance, use the `MemoryLayout<T>.stride` static property instead.

```swift
let x: Int = 100

// Finding the alignment of a value's type
let s = MemoryLayout.alignment(ofValue: x)
// s == 8

// Finding the alignment of a type directly
let t = MemoryLayout<Int>.alignment
// t == 8
```

## Parameters

- `value`: A value representative of the type to describe.

## See Also

- [static func stride(ofValue: borrowing T) -> Int](memorylayout/stride(ofvalue:).md)
  Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [static func size(ofValue: borrowing T) -> Int](memorylayout/size(ofvalue:).md)
  Returns the contiguous memory footprint of the given instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/memorylayout/alignment(ofvalue:))*