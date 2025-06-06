# CFArrayGetValueAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Retrieves a value at a given index.

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
func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafeRawPointer!
```

#### Return Value

The value at the `idx` index in `theArray`. If the return value is a Core Foundation Object, ownership follows [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `theArray`: The array to examine.
- `idx`: The index of the value to retrieve. If the index is outside the index space of   (  to   inclusive (where   is the count of  ), the behavior is undefined.

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
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfarraygetvalues(_:_:_:).md)
  Fills a buffer with values from an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetvalueatindex(_:_:))*