# version

**Framework**: Core Foundation  
**Kind**: property

The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.

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
var version: CFIndex
```

## See Also

- [typealias CFBinaryHeapApplierFunction](cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!](cfbinaryheapcallbacks/compare.md)
  The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfbinaryheapcallbacks/copydescription.md)
  Callback function used to get a description of a value in a binary heap.
- [var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!](cfbinaryheapcallbacks/release.md)
  Callback function used to release a value before it is removed from a binary heap.
- [var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfbinaryheapcallbacks/retain.md)
  Callback function used to retain a value being added to a binary heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/version)*