# CFArrayAppendValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a value to an array giving it the new largest index.

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
func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: UnsafeRawPointer!)
```

```c
extern void CFArrayAppendValue(CFMutableArrayRef theArray, const void *value);
```

## Discussion

The `value` parameter is retained by `theArray` using the retain callback provided when `theArray` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. The `value` parameter is assigned to the index one larger than the previous largest index and the count of `theArray` is increased by one.

## Parameters

- `theArray`: The array to which `value` is to be added. If `theArray` is a limited-capacity array and it is full before this operation, the behavior is undefined.
- `value`: A CFType object or a pointer value to add to `theArray`.

## See Also

### CFMutableArray Miscellaneous Functions
- [func CFArrayAppendArray(CFMutableArray!, CFArray!, CFRange)](./cfarrayappendarray%28_,_,_%29.md)
  Adds the values from one array to another array.
- [func CFArrayCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!](./cfarraycreatemutable%28_,_,_%29.md)
  Creates a new empty mutable array.
- [func CFArrayCreateMutableCopy(CFAllocator!, CFIndex, CFArray!) -> CFMutableArray!](./cfarraycreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable array with the values from another array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayappendvalue(_:_:))*