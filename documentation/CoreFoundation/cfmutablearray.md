# CFMutableArray

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

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
class CFMutableArray
```

```c
typedef struct __CFArray * CFMutableArrayRef;
```

#### Overview

CFMutableArray manages dynamic arrays. The basic interface for managing arrays is provided by [`CFArray`](./cfarray.md). CFMutableArray adds functions to modify the contents of an array.

You create a mutable array object using either the [`CFArrayCreateMutable(_:_:_:)`](./cfarraycreatemutable%28_,_,_%29.md) or [`CFArrayCreateMutableCopy(_:_:_:)`](./cfarraycreatemutablecopy%28_,_,_%29.md) function.

CFMutableArray provides several functions for changing the contents of an array, for example the [`CFArrayAppendValue(_:_:)`](./cfarrayappendvalue%28_,_%29.md) and [`CFArrayInsertValueAtIndex(_:_:_:)`](./cfarrayinsertvalueatindex%28_,_,_%29.md) functions add values to an array and [`CFArrayRemoveValueAtIndex(_:_:)`](./cfarrayremovevalueatindex%28_,_%29.md) removes values from an array. You can also reorder the contents of an array using [`CFArrayExchangeValuesAtIndices(_:_:_:)`](./cfarrayexchangevaluesatindices%28_,_,_%29.md) and [`CFArraySortValues(_:_:_:_:)`](./cfarraysortvalues%28_,_,_,_%29.md).

CFMutableArray is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableArray`](../Foundation/nsmutablearray.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableArray *` parameter, you can pass in a `CFMutableArrayRef`, and in a function where you see a `CFMutableArrayRef` parameter, you can pass in an NSMutableArray instance. This fact also applies to concrete subclasses of NSMutableArray. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

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

## Relationships

### Inherits From
- [CFArray](./cfarray.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablearray)*