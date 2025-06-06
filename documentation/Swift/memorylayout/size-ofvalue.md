# size(ofValue:)

**Framework**: Swift  
**Kind**: method

Returns the contiguous memory footprint of the given instance.

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
static func size(ofValue value: borrowing T) -> Int
```

#### Return Value

The size, in bytes, of the given value’s type.

#### Discussion

The result does not include any dynamically allocated or out of line storage. In particular, pointers and class instances all have the same contiguous memory footprint, regardless of the size of the referenced data.

When you have a type instead of an instance, use the `MemoryLayout<T>.size` static property instead.

```swift
let x: Int = 100

// Finding the size of a value's type
let s = MemoryLayout.size(ofValue: x)
// s == 8

// Finding the size of a type directly
let t = MemoryLayout<Int>.size
// t == 8
```

## Parameters

- `value`: A value representative of the type to describe.

## See Also

- [static func stride(ofValue: borrowing T) -> Int](memorylayout/stride(ofvalue:).md)
  Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [static func alignment(ofValue: borrowing T) -> Int](memorylayout/alignment(ofvalue:).md)
  Returns the default memory alignment of `T`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/memorylayout/size(ofvalue:))*