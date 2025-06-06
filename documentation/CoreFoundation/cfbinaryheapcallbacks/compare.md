# compare

**Framework**: Core Foundation  
**Kind**: property

The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.

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
var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!
```

#### Return Value

[`CFComparisonResult.compareLessThan`](cfcomparisonresult/comparelessthan.md) if `ptr1` is less than `ptr2`, [`CFComparisonResult.compareEqualTo`](cfcomparisonresult/compareequalto.md) if `ptr1` and `ptr2` are equal, or [`CFComparisonResult.compareGreaterThan`](cfcomparisonresult/comparegreaterthan.md) if `ptr1` is greater than `ptr2`.

## Parameters

- `ptr1`: First value to compare.
- `ptr2`: Second value to compare.
- `info`: Not used. Should always be  .

## See Also

- [typealias CFBinaryHeapApplierFunction](cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfbinaryheapcallbacks/copydescription.md)
  Callback function used to get a description of a value in a binary heap.
- [var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!](cfbinaryheapcallbacks/release.md)
  Callback function used to release a value before it is removed from a binary heap.
- [var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfbinaryheapcallbacks/retain.md)
  Callback function used to retain a value being added to a binary heap.
- [var version: CFIndex](cfbinaryheapcallbacks/version.md)
  The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks/compare)*