# CFBinaryHeapCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable or fixed-mutable binary heap.

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
func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBinaryHeapCallBacks>!, _ compareContext: UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!
```

#### Return Value

A new `CFBinaryHeap` object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the binary heap. The binary heap starts empty and can grow to this number of values. If this parameter is  , the binary heap’s maximum capacity is limited only by memory.
- `callBacks`: A pointer to a   structure initialized with the callbacks that operate on the values placed into the binary heap. If the binary heap will be holding   objects, pass the   constant. This functions makes a copy of the contents of the callbacks structure, so that a pointer to a structure on the stack can be passed in, or can be reused for multiple binary heap creations. This callbacks parameter may not be  .
- `compareContext`: Not used. Pass  .

## See Also

- [func CFBinaryHeapAddValue(CFBinaryHeap!, UnsafeRawPointer!)](cfbinaryheapaddvalue(_:_:).md)
  Adds a value to a binary heap.
- [func CFBinaryHeapApplyFunction(CFBinaryHeap!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfbinaryheapapplyfunction(_:_:_:).md)
  Iteratively applies a function to all the values in a binary heap.
- [func CFBinaryHeapContainsValue(CFBinaryHeap!, UnsafeRawPointer!) -> Bool](cfbinaryheapcontainsvalue(_:_:).md)
  Returns whether a given value is in a binary heap.
- [func CFBinaryHeapCreateCopy(CFAllocator!, CFIndex, CFBinaryHeap!) -> CFBinaryHeap!](cfbinaryheapcreatecopy(_:_:_:).md)
  Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.
- [func CFBinaryHeapGetCount(CFBinaryHeap!) -> CFIndex](cfbinaryheapgetcount(_:).md)
  Returns the number of values currently in a binary heap.
- [func CFBinaryHeapGetCountOfValue(CFBinaryHeap!, UnsafeRawPointer!) -> CFIndex](cfbinaryheapgetcountofvalue(_:_:).md)
  Counts the number of times a given value occurs in a binary heap.
- [func CFBinaryHeapGetMinimum(CFBinaryHeap!) -> UnsafeRawPointer!](cfbinaryheapgetminimum(_:).md)
  Returns the minimum value in a binary heap.
- [func CFBinaryHeapGetMinimumIfPresent(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfbinaryheapgetminimumifpresent(_:_:).md)
  Returns the minimum value in a binary heap, if present.
- [func CFBinaryHeapGetTypeID() -> CFTypeID](cfbinaryheapgettypeid().md)
  Returns the type identifier of the `CFBinaryHeap` opaque type.
- [func CFBinaryHeapGetValues(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbinaryheapgetvalues(_:_:).md)
  Copies all the values from a binary heap into a sorted C array.
- [func CFBinaryHeapRemoveAllValues(CFBinaryHeap!)](cfbinaryheapremoveallvalues(_:).md)
  Removes all values from a binary heap, making it empty.
- [func CFBinaryHeapRemoveMinimumValue(CFBinaryHeap!)](cfbinaryheapremoveminimumvalue(_:).md)
  Removes the minimum value from a binary heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcreate(_:_:_:_:))*