# CFArrayInsertValueAtIndex(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Inserts a value into an array at a given index.

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
func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!)
```

```c
extern void CFArrayInsertValueAtIndex(CFMutableArrayRef theArray, CFIndex idx, const void *value);
```

## Discussion

The `value` parameter is assigned to the index `idx`, and all values in `theArray` with equal and larger indices have their indices increased by one.

## Parameters

- `theArray`: The array into which `value` is inserted. If `theArray` is a fixed-capacity array and it is full before this operation, the behavior is undefined.
- `idx`: The index at which to insert `value`. The index must be in the range `0` to `N` inclusive, where `N` is the count of `theArray` before the operation. If the index is the same as the count of `theArray`, this function has the same effect as [`CFArrayAppendValue(_:_:)`](./cfarrayappendvalue%28_,_%29.md).
- `value`: The value to insert into `theArray`. The value is retained by `theArray` using the retain callback provided when `theArray` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined.

## See Also

### CFMutableArray Miscellaneous Functions
- [func CFArrayAppendArray(CFMutableArray!, CFArray!, CFRange)](./cfarrayappendarray%28_,_,_%29.md)
  Adds the values from one array to another array.
- [func CFArrayAppendValue(CFMutableArray!, UnsafeRawPointer!)](./cfarrayappendvalue%28_,_%29.md)
  Adds a value to an array giving it the new largest index.
- [func CFArrayCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!](./cfarraycreatemutable%28_,_,_%29.md)
  Creates a new empty mutable array.
- [func CFArrayCreateMutableCopy(CFAllocator!, CFIndex, CFArray!) -> CFMutableArray!](./cfarraycreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable array with the values from another array.
- [func CFArrayExchangeValuesAtIndices(CFMutableArray!, CFIndex, CFIndex)](./cfarrayexchangevaluesatindices%28_,_,_%29.md)
  Exchanges the values at two indices of an array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayinsertvalueatindex(_:_:_:))*