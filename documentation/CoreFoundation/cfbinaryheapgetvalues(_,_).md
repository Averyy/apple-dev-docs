# CFBinaryHeapGetValues(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Copies all the values from a binary heap into a sorted C array.

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
func CFBinaryHeapGetValues(_ heap: CFBinaryHeap!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

```c
extern void CFBinaryHeapGetValues(CFBinaryHeapRef heap, const void **values);
```

## Parameters

- `heap`: The binary heap to use.
- `values`: On return, the memory pointed to by this argument holds a C array of all the values in heap, sorted from minimum to maximum values. You must allocate sufficient memory to hold all the values in `heap` before calling this function. If the values are Core Foundation objects, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

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
- [func CFBinaryHeapCreateCopy(CFAllocator!, CFIndex, CFBinaryHeap!) -> CFBinaryHeap!](./cfbinaryheapcreatecopy%28_,_,_%29.md)
  Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.
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
- [func CFBinaryHeapRemoveAllValues(CFBinaryHeap!)](./cfbinaryheapremoveallvalues%28_%29.md)
  Removes all values from a binary heap, making it empty.
- [func CFBinaryHeapRemoveMinimumValue(CFBinaryHeap!)](./cfbinaryheapremoveminimumvalue%28_%29.md)
  Removes the minimum value from a binary heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapgetvalues(_:_:))*