# CFBinaryHeapRemoveMinimumValue(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes the minimum value from a binary heap.

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
func CFBinaryHeapRemoveMinimumValue(_ heap: CFBinaryHeap!)
```

```c
extern void CFBinaryHeapRemoveMinimumValue(CFBinaryHeapRef heap);
```

#### Discussion

If `heap` contains several equal minimum values, only one of them is removed. If `heap` is empty, this function does nothing.

## Parameters

- `heap`: The binary heap to use.

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
- [func CFBinaryHeapGetValues(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfbinaryheapgetvalues%28_,_%29.md)
  Copies all the values from a binary heap into a sorted C array.
- [func CFBinaryHeapRemoveAllValues(CFBinaryHeap!)](./cfbinaryheapremoveallvalues%28_%29.md)
  Removes all values from a binary heap, making it empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapremoveminimumvalue(_:))*