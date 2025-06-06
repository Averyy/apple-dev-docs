# CFBinaryHeap

**Framework**: Core Foundation  
**Kind**: class

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
class CFBinaryHeap
```

#### Overview

`CFBinaryHeap` implements a container that stores values sorted using a binary search algorithm. All binary heaps are mutable; there is not a separate immutable variety. Binary heaps can be useful as priority queues.

## Topics

### CFBinaryHeap Miscellaneous Functions
- [func CFBinaryHeapAddValue(CFBinaryHeap!, UnsafeRawPointer!)](cfbinaryheapaddvalue(_:_:).md)
  Adds a value to a binary heap.
- [func CFBinaryHeapApplyFunction(CFBinaryHeap!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfbinaryheapapplyfunction(_:_:_:).md)
  Iteratively applies a function to all the values in a binary heap.
- [func CFBinaryHeapContainsValue(CFBinaryHeap!, UnsafeRawPointer!) -> Bool](cfbinaryheapcontainsvalue(_:_:).md)
  Returns whether a given value is in a binary heap.
- [func CFBinaryHeapCreate(CFAllocator!, CFIndex, UnsafePointer<CFBinaryHeapCallBacks>!, UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!](cfbinaryheapcreate(_:_:_:_:).md)
  Creates a new mutable or fixed-mutable binary heap.
- [func CFBinaryHeapCreateCopy(CFAllocator!, CFIndex, CFBinaryHeap!) -> CFBinaryHeap!](cfbinaryheapcreatecopy(_:_:_:).md)
  Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.
- [func CFBinaryHeapGetCount(CFBinaryHeap!) -> CFIndex](cfbinaryheapgetcount(_:).md)
  Returns the number of values currently in a binary heap.
- [func CFBinaryHeapGetCountOfValue(CFBinaryHeap!, UnsafeRawPointer!) -> CFIndex](cfbinaryheapgetcountofvalue(_:_:).md)
  Counts the number of times a given value occurs in a binary heap.
- [func CFBinaryHeapGetMinimum(CFBinaryHeap!) -> UnsafeRawPointer!](cfbinaryheapgetminimum(_:).md)
  Returns the minimum value in a binary heap.
- [func CFBinaryHeapGetMinimumIfPresent(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfbinaryheapgetminimumifpresent(_:_:).md)
  Returns the minimum value in a binary heap, if present.
- [func CFBinaryHeapGetTypeID() -> CFTypeID](cfbinaryheapgettypeid().md)
  Returns the type identifier of the `CFBinaryHeap` opaque type.
- [func CFBinaryHeapGetValues(CFBinaryHeap!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbinaryheapgetvalues(_:_:).md)
  Copies all the values from a binary heap into a sorted C array.
- [func CFBinaryHeapRemoveAllValues(CFBinaryHeap!)](cfbinaryheapremoveallvalues(_:).md)
  Removes all values from a binary heap, making it empty.
- [func CFBinaryHeapRemoveMinimumValue(CFBinaryHeap!)](cfbinaryheapremoveminimumvalue(_:).md)
  Removes the minimum value from a binary heap.
### Callbacks
- [typealias CFBinaryHeapApplierFunction](cfbinaryheapapplierfunction.md)
  Callback function used to apply a function to all members of a binary heap.
- [var compare: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult)!](cfbinaryheapcallbacks/compare.md)
  The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfbinaryheapcallbacks/copydescription.md)
  Callback function used to get a description of a value in a binary heap.
- [var release: ((CFAllocator?, UnsafeRawPointer?) -> Void)!](cfbinaryheapcallbacks/release.md)
  Callback function used to release a value before it is removed from a binary heap.
- [var retain: ((CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfbinaryheapcallbacks/retain.md)
  Callback function used to retain a value being added to a binary heap.
- [var version: CFIndex](cfbinaryheapcallbacks/version.md)
  The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.
### Data Types
- [struct CFBinaryHeapCallBacks](cfbinaryheapcallbacks.md)
  Structure containing the callbacks for values for a `CFBinaryHeap` object.
- [struct CFBinaryHeapCompareContext](cfbinaryheapcomparecontext.md)
  Not used.
### Constants
- [Predefined Callback Structures](cfbinaryheap-predefined-callback-structures.md)
  `CFBinaryHeap` provides some predefined callbacks for your convenience.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Collections Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbinaryheap)*