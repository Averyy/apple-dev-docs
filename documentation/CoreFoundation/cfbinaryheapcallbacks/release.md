# release

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

Callback function used to release a value before it is removed from a binary heap.

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
var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!
```

```c
void (*)(const struct __CFAllocator *, const void *) release;
```

#### Discussion

The callback used to remove a retain previously added for the binary heap from values as they are removed from the binary heap. If this field is `NULL`, the binary heap does nothing to release a value being removed.

## Parameters

- `allocator`: The binary heap’s allocator.
- `ptr`: The value to release.

## See Also

### Callbacks
- [typealias CFBinaryHeapApplierFunction](../cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!](./compare.md)
  The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](./copydescription.md)
  Callback function used to get a description of a value in a binary heap.
- [var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!](./retain.md)
  Callback function used to retain a value being added to a binary heap.
- [var version: CFIndex](./version.md)
  The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/release)*