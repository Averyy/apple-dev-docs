# CFMutableBag

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
class CFMutableBag
```

```c
typedef struct __CFBag * CFMutableBagRef;
```

#### Overview

CFMutableBag manages dynamic bags. The basic interface for managing bags is provided by [`CFBag`](./cfbag.md). CFMutableBag adds functions to modify the contents of a bag.

You create a mutable bag object using either the [`CFBagCreateMutable(_:_:_:)`](./cfbagcreatemutable%28_,_,_%29.md) or [`CFBagCreateMutableCopy(_:_:_:)`](./cfbagcreatemutablecopy%28_,_,_%29.md) function.

CFMutableBag provides several functions for adding and removing values from a bag. The [`CFBagAddValue(_:_:)`](./cfbagaddvalue%28_,_%29.md) function adds a value to a bag and [`CFBagRemoveValue(_:_:)`](./cfbagremovevalue%28_,_%29.md) removes values from a bag.

## Topics

### Creating a Mutable Bag
- [func CFBagCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFBagCallBacks>!) -> CFMutableBag!](./cfbagcreatemutable%28_,_,_%29.md)
  Creates a new empty mutable bag.
- [func CFBagCreateMutableCopy(CFAllocator!, CFIndex, CFBag!) -> CFMutableBag!](./cfbagcreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable bag with the values from another bag.
### Modifying a Mutable Bag
- [func CFBagAddValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagaddvalue%28_,_%29.md)
  Adds a value to a mutable bag.
- [func CFBagRemoveAllValues(CFMutableBag!)](./cfbagremoveallvalues%28_%29.md)
  Removes all values from a mutable bag.
- [func CFBagRemoveValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagremovevalue%28_,_%29.md)
  Removes a value from a mutable bag.
- [func CFBagReplaceValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagreplacevalue%28_,_%29.md)
  Replaces a value in a mutable bag.
- [func CFBagSetValue(CFMutableBag!, UnsafeRawPointer!)](./cfbagsetvalue%28_,_%29.md)
  Sets a value in a mutable bag.

## Relationships

### Inherits From
- [CFBag](./cfbag.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablebag)*