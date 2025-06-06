# retain

**Framework**: Core Foundation  
**Kind**: property

Callback function used to retain a value being added to a binary heap.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!
```

#### Return Value

The value to store in the binary heap, which is usually the `ptr` parameter passed to this callback, but may be a different   value if a different value should be stored in the binary heap.

#### Discussion

The callback used to add a retain for the binary heap on values as they are put into the binary heap. This callback returns the value to use as the value in the binary heap, which is usually the value parameter passed to this callback, but may be a different value if a different value should be added to the binary heap. If this field is `NULL`, the binary heap does nothing to retain a value being added.

## Parameters

- `allocator`: The binary heap’s allocator.
- `ptr`: The value to retain.

## See Also

- [typealias CFBinaryHeapApplierFunction](cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!](cfbinaryheapcallbacks/compare.md)
  The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfbinaryheapcallbacks/copydescription.md)
  Callback function used to get a description of a value in a binary heap.
- [var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!](cfbinaryheapcallbacks/release.md)
  Callback function used to release a value before it is removed from a binary heap.
- [var version: CFIndex](cfbinaryheapcallbacks/version.md)
  The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/retain)*