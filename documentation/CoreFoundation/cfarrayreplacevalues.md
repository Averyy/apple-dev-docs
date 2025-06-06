# CFArrayReplaceValues(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces a range of values in an array.

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
func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafeMutablePointer<UnsafeRawPointer?>!, _ newCount: CFIndex)
```

## Parameters

- `theArray`: The array in which some values are to be replaced. If this parameter is not a valid CFMutableArray object, the behavior is undefined.
- `range`: The range of values within   to replace. The range location or end point (defined by the location plus length minus 1) must not lie outside the index space of   (  to   inclusive, where   is the count of  ). The range length must not be negative. The range may be empty (length 0), in which case the new values are merely inserted at the range location.
- `newValues`: A C array of the pointer-sized values to be placed into  . The new values in   are ordered in the same order in which they appear in this C array. This parameter may be   if the   parameter is 0. This C array is not changed or freed by this function. If this parameter is not a valid pointer to a C array of at least   pointers, the behavior is undefined.
- `newCount`: The number of values to copy from the   C array into  . If this parameter is different from the range length, the excess   values are inserted after the range or the excess range values are deleted. This parameter may be 0, in which case no new values are replaced into   and the values in the range are simply removed. If this parameter is negative or greater than the number of values actually in the   C array, the behavior is undefined.

## See Also

- [func CFArrayAppendArray(CFMutableArray!, CFArray!, CFRange)](cfarrayappendarray(_:_:_:).md)
  Adds the values from one array to another array.
- [func CFArrayAppendValue(CFMutableArray!, UnsafeRawPointer!)](cfarrayappendvalue(_:_:).md)
  Adds a value to an array giving it the new largest index.
- [func CFArrayCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!](cfarraycreatemutable(_:_:_:).md)
  Creates a new empty mutable array.
- [func CFArrayCreateMutableCopy(CFAllocator!, CFIndex, CFArray!) -> CFMutableArray!](cfarraycreatemutablecopy(_:_:_:).md)
  Creates a new mutable array with the values from another array.
- [func CFArrayExchangeValuesAtIndices(CFMutableArray!, CFIndex, CFIndex)](cfarrayexchangevaluesatindices(_:_:_:).md)
  Exchanges the values at two indices of an array.
- [func CFArrayInsertValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](cfarrayinsertvalueatindex(_:_:_:).md)
  Inserts a value into an array at a given index.
- [func CFArrayRemoveAllValues(CFMutableArray!)](cfarrayremoveallvalues(_:).md)
  Removes all the values from an array, making it empty.
- [func CFArrayRemoveValueAtIndex(CFMutableArray!, CFIndex)](cfarrayremovevalueatindex(_:_:).md)
  Removes the value at a given index from an array.
- [func CFArraySetValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](cfarraysetvalueatindex(_:_:_:).md)
  Changes the value at a given index in an array.
- [func CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction!, UnsafeMutableRawPointer!)](cfarraysortvalues(_:_:_:_:).md)
  Sorts the values in an array using a given comparison function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayreplacevalues(_:_:_:_:))*