# CFArrayCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new mutable array with the values from another array.

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
func CFArrayCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theArray: CFArray!) -> CFMutableArray!
```

```c
extern CFMutableArrayRefCFArrayCreateMutableCopy(CFAllocatorRef allocator, CFIndex capacity, CFArrayRef theArray);
```

## Return Value

A new mutable array that contains the same values as `theArray`. The new array has the same count as the `theArray` and uses the same callbacks. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new array and its storage for values. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `capacity`: The maximum number of values that can be contained by the new array. The array starts with the same number of values as `theArray` and can grow to this number of values (and it can have less).

  Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theArray`.
- `theArray`: The array to copy. The pointer values from the array are copied into the new array. However, the values are also retained by the new array.

## See Also

### CFMutableArray Miscellaneous Functions
- [func CFArrayAppendArray(CFMutableArray!, CFArray!, CFRange)](./cfarrayappendarray%28_,_,_%29.md)
  Adds the values from one array to another array.
- [func CFArrayAppendValue(CFMutableArray!, UnsafeRawPointer!)](./cfarrayappendvalue%28_,_%29.md)
  Adds a value to an array giving it the new largest index.
- [func CFArrayCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!](./cfarraycreatemutable%28_,_,_%29.md)
  Creates a new empty mutable array.
- [func CFArrayExchangeValuesAtIndices(CFMutableArray!, CFIndex, CFIndex)](./cfarrayexchangevaluesatindices%28_,_,_%29.md)
  Exchanges the values at two indices of an array.
- [func CFArrayInsertValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](./cfarrayinsertvalueatindex%28_,_,_%29.md)
  Inserts a value into an array at a given index.
- [func CFArrayRemoveAllValues(CFMutableArray!)](./cfarrayremoveallvalues%28_%29.md)
  Removes all the values from an array, making it empty.
- [func CFArrayRemoveValueAtIndex(CFMutableArray!, CFIndex)](./cfarrayremovevalueatindex%28_,_%29.md)
  Removes the value at a given index from an array.
- [func CFArrayReplaceValues(CFMutableArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex)](./cfarrayreplacevalues%28_,_,_,_%29.md)
  Replaces a range of values in an array.
- [func CFArraySetValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](./cfarraysetvalueatindex%28_,_,_%29.md)
  Changes the value at a given index in an array.
- [func CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction!, UnsafeMutableRawPointer!)](./cfarraysortvalues%28_,_,_,_%29.md)
  Sorts the values in an array using a given comparison function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycreatemutablecopy(_:_:_:))*