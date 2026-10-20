# CFArrayExchangeValuesAtIndices(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Exchanges the values at two indices of an array.

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
func CFArrayExchangeValuesAtIndices(_ theArray: CFMutableArray!, _ idx1: CFIndex, _ idx2: CFIndex)
```

```c
extern void CFArrayExchangeValuesAtIndices(CFMutableArrayRef theArray, CFIndex idx1, CFIndex idx2);
```

## Parameters

- `theArray`: The array that contains the values to be swapped.
- `idx1`: The index of the value to swap with the value at `idx2`. The index must not exceed the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray` before the operation).
- `idx2`: The index of the value to swap with the value at `idx1`. The index must not exceed the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray` before the operation).

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayexchangevaluesatindices(_:_:_:))*