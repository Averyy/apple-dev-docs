# copyDescription

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

Callback function used to get a description of a value in a binary heap.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!
```

```c
const struct __CFString *(*)(const void *) copyDescription;
```

#### Discussion

The callback used to create a descriptive string representation of each value in the binary heap. This is used by the [`CFCopyDescription(_:)`](../cfcopydescription%28_%29.md) function. If this field is `NULL`, the binary heap constructs a `CFString` object describing the value based on its pointer value.

## Parameters

- `ptr`: The value to be described.

## See Also

### Callbacks
- [typealias CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!](./compare.md)
  The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!](./release.md)
  Callback function used to release a value before it is removed from a binary heap.
- [var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!](./retain.md)
  Callback function used to retain a value being added to a binary heap.
- [var version: CFIndex](./version.md)
  The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/copydescription)*