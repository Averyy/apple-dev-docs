# CFArrayGetValues(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Fills a buffer with values from an array.

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
func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theArray`: The array to examine.
- `range`: The range of values within `theArray` to retrieve. The range must lie within the bounds of `theArray`. The range may be empty (length `0`), in which case no values are put into the buffer `values`.
- `values`: A C array of pointer-sized values to be filled with values from `theArray`. The values in the C array are in the same order as they appear in `theArray`. If this value is not a valid pointer to a C array of at least `range.length` pointers, the behavior is undefined. If the values are Core Foundation objects, ownership follows [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

- [func CFArrayBSearchValues(CFArray!, CFRange, UnsafeRawPointer!, CFComparatorFunction!, UnsafeMutableRawPointer!) -> CFIndex](cfarraybsearchvalues(_:_:_:_:_:).md)
  Searches an array for a value using a binary search algorithm.
- [func CFArrayContainsValue(CFArray!, CFRange, UnsafeRawPointer!) -> Bool](cfarraycontainsvalue(_:_:_:).md)
  Reports whether or not a value is in an array.
- [func CFArrayGetCount(CFArray!) -> CFIndex](cfarraygetcount(_:).md)
  Returns the number of values currently in an array.
- [func CFArrayGetCountOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetcountofvalue(_:_:_:).md)
  Counts the number of times a given value occurs in an array.
- [func CFArrayGetFirstIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetfirstindexofvalue(_:_:_:).md)
  Searches an array forward for a value.
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetlastindexofvalue(_:_:_:).md)
  Searches an array backward for a value.
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](cfarraygetvalueatindex(_:_:).md)
  Retrieves a value at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetvalues(_:_:_:))*