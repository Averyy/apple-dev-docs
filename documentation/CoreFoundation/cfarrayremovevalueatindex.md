# CFArrayRemoveValueAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes the value at a given index from an array.

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
func CFArrayRemoveValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex)
```

#### Discussion

All values in `theArray` with indices larger than `idx` have their indices decreased by one.

## Parameters

- `theArray`: The array from which the value is removed.
- `idx`: The index of the value to remove. The index must be in the range 0 to N-1 inclusive, where N is the count of   before the operation.

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
- [func CFArrayReplaceValues(CFMutableArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex)](cfarrayreplacevalues(_:_:_:_:).md)
  Replaces a range of values in an array.
- [func CFArraySetValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](cfarraysetvalueatindex(_:_:_:).md)
  Changes the value at a given index in an array.
- [func CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction!, UnsafeMutableRawPointer!)](cfarraysortvalues(_:_:_:_:).md)
  Sorts the values in an array using a given comparison function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayremovevalueatindex(_:_:))*