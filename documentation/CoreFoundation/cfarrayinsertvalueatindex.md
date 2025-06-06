# CFArrayInsertValueAtIndex(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Inserts a value into an array at a given index.

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
func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!)
```

#### Discussion

The `value` parameter is assigned to the index `idx`, and all values in `theArray` with equal and larger indices have their indices increased by one.

## Parameters

- `theArray`: The array into which   is inserted. If   is a fixed-capacity array and it is full before this operation, the behavior is undefined.
- `idx`: The index at which to insert  . The index must be in the range   to   inclusive, where   is the count of   before the operation. If the index is the same as the count of  , this function has the same effect as  .
- `value`: The value to insert into  . The value is retained by   using the retain callback provided when   was created. If   is not of the type expected by the retain callback, the behavior is undefined.

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
- [func CFArrayRemoveAllValues(CFMutableArray!)](cfarrayremoveallvalues(_:).md)
  Removes all the values from an array, making it empty.
- [func CFArrayRemoveValueAtIndex(CFMutableArray!, CFIndex)](cfarrayremovevalueatindex(_:_:).md)
  Removes the value at a given index from an array.
- [func CFArrayReplaceValues(CFMutableArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex)](cfarrayreplacevalues(_:_:_:_:).md)
  Replaces a range of values in an array.
- [func CFArraySetValueAtIndex(CFMutableArray!, CFIndex, UnsafeRawPointer!)](cfarraysetvalueatindex(_:_:_:).md)
  Changes the value at a given index in an array.
- [func CFArraySortValues(CFMutableArray!, CFRange, CFComparatorFunction!, UnsafeMutableRawPointer!)](cfarraysortvalues(_:_:_:_:).md)
  Sorts the values in an array using a given comparison function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayinsertvalueatindex(_:_:_:))*