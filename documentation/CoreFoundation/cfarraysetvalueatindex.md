# CFArraySetValueAtIndex(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Changes the value at a given index in an array.

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
func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!)
```

## Parameters

- `theArray`: The array in which the value is to be changed.
- `idx`: The index at which to set the new value. The value must not lie outside the index space of   (  to   inclusive, where   is the count of the array before the operation).
- `value`: The value to set in  . The value is retained by   using the retain callback provided when   was created and the previous value at   is released. If the value is not of the type expected by the retain callback, the behavior is undefined. The indices of other values are not affected.

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
- [func CFArrayReplaceValues(CFMutableArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex)](cfarrayreplacevalues(_:_:_:_:).md)
  Replaces a range of values in an array.
- [func CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction!, UnsafeMutableRawPointer!)](cfarraysortvalues(_:_:_:_:).md)
  Sorts the values in an array using a given comparison function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraysetvalueatindex(_:_:_:))*