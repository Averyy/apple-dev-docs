# CFBinaryHeapContainsValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns whether a given value is in a binary heap.

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
func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!) -> Bool
```

#### Return Value

`true` if `value` is a member of `heap`, `false` otherwise.

## Parameters

- `heap`: The binary heap to search.
- `value`: The value for which to find matches in the binary heap. The compare callback provided in the   structure when the binary heap was created is used to compare values. If  , or any of the values in the binary heap, are not understood by the compare callback, the behavior is undefined.

## See Also

- [func CFBinaryHeapAddValue(CFBinaryHeap!, UnsafeRawPointer!)](cfbinaryheapaddvalue(_:_:).md)
  Adds a value to a binary heap.
- [func CFBinaryHeapApplyFunction(CFBinaryHeap!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfbinaryheapapplyfunction(_:_:_:).md)
  Iteratively applies a function to all the values in a binary heap.
- [func CFBinaryHeapCreate(CFAllocator!, CFIndex, UnsafePointer<CFBinaryHeapCallBacks>!, UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!](cfbinaryheapcreate(_:_:_:_:).md)
  Creates a new mutable or fixed-mutable binary heap.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheapcontainsvalue(_:_:))*