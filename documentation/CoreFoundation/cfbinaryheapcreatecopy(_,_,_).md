# CFBinaryHeapCreateCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.

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
func CFBinaryHeapCreateCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ heap: CFBinaryHeap!) -> CFBinaryHeap!
```

```c
extern CFBinaryHeapRefCFBinaryHeapCreateCopy(CFAllocatorRef allocator, CFIndex capacity, CFBinaryHeapRef heap);
```

#### Return Value

A new `CFBinaryHeap` object holding the same values as `heap`. The new binary heap uses the same callbacks as `heap`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the binary heap. The binary heap starts with the same number of values as `heap` and can grow to this number of values. If this parameter is `0`, the binary heap’s maximum capacity is limited only by memory. If nonzero, `capacity` must be large enough to hold all the values in `heap`.
- `heap`: The binary heap which is to be copied. The values from the binary heap are copied as pointers into the new binary heap (that is, the values themselves are copied, not that to which the values point, if anything). However, the values are also retained by the new binary heap.

## See Also

### CFBinaryHeap Miscellaneous Functions
- [func CFBinaryHeapAddValue(CFBinaryHeap!, UnsafeRawPointer!)](./cfbinaryheapaddvalue%28_,_%29.md)
  Adds a value to a binary heap.
- [func CFBinaryHeapApplyFunction(CFBinaryHeap!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](./cfbinaryheapapplyfunction%28_,_,_%29.md)
  Iteratively applies a function to all the values in a binary heap.
- [func CFBinaryHeapContainsValue(CFBinaryHeap!, UnsafeRawPointer!) -> Bool](./cfbinaryheapcontainsvalue%28_,_%29.md)
  Returns whether a given value is in a binary heap.
- [func CFBinaryHeapCreate(CFAllocator!, CFIndex, UnsafePointer<CFBinaryHeapCallBacks>!, UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!](./cfbinaryheapcreate%28_,_,_,_%29.md)
  Creates a new mutable or fixed-mutable binary heap.
- [func CFBinaryHeapGetCount(CFBinaryHeap!) -> CFIndex](./cfbinaryheapgetcount%28_%29.md)
  Returns the number of values currently in a binary heap.
- [func CFBinaryHeapGetCountOfValue(CFBinaryHeap!, UnsafeRawPointer!) -> CFIndex](./cfbinaryheapgetcountofvalue%28_,_%29.md)
  Counts the number of times a given value occurs in a binary heap.
- [func CFBinaryHeapGetMinimum(CFBinaryHeap!) -> UnsafeRawPointer!](./cfbinaryheapgetminimum%28_%29.md)
  Returns the minimum value in a binary heap.
- [func CFBinaryHeapGetMinimumIfPresent(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfbinaryheapgetminimumifpresent%28_,_%29.md)
  Returns the minimum value in a binary heap, if present.
- [func CFBinaryHeapGetTypeID() -> CFTypeID](./cfbinaryheapgettypeid%28%29.md)
  Returns the type identifier of the `CFBinaryHeap` opaque type.
- [func CFBinaryHeapGetValues(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfbinaryheapgetvalues%28_,_%29.md)
  Copies all the values from a binary heap into a sorted C array.
- [func CFBinaryHeapRemoveAllValues(CFBinaryHeap!)](./cfbinaryheapremoveallvalues%28_%29.md)
  Removes all values from a binary heap, making it empty.
- [func CFBinaryHeapRemoveMinimumValue(CFBinaryHeap!)](./cfbinaryheapremoveminimumvalue%28_%29.md)
  Removes the minimum value from a binary heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcreatecopy(_:_:_:))*