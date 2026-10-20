# CFArrayGetValueAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Retrieves a value at a given index.

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
func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafeRawPointer!
```

```c
extern const void *CFArrayGetValueAtIndex(CFArrayRef theArray, CFIndex idx);
```

#### Return Value

The value at the `idx` index in `theArray`. If the return value is a Core Foundation Object, ownership follows [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `theArray`: The array to examine.
- `idx`: The index of the value to retrieve. If the index is outside the index space of `theArray` (`0` to `N-1` inclusive (where `N` is the count of `theArray`), the behavior is undefined.

## See Also

### Examining an Array
- [func CFArrayBSearchValues(CFArray!, CFRange, UnsafeRawPointer!, CFComparatorFunction!, UnsafeMutableRawPointer!) -> CFIndex](./cfarraybsearchvalues%28_,_,_,_,_%29.md)
  Searches an array for a value using a binary search algorithm.
- [func CFArrayContainsValue(CFArray!, CFRange, UnsafeRawPointer!) -> Bool](./cfarraycontainsvalue%28_,_,_%29.md)
  Reports whether or not a value is in an array.
- [func CFArrayGetCount(CFArray!) -> CFIndex](./cfarraygetcount%28_%29.md)
  Returns the number of values currently in an array.
- [func CFArrayGetCountOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetcountofvalue%28_,_,_%29.md)
  Counts the number of times a given value occurs in an array.
- [func CFArrayGetFirstIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetfirstindexofvalue%28_,_,_%29.md)
  Searches an array forward for a value.
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetlastindexofvalue%28_,_,_%29.md)
  Searches an array backward for a value.
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfarraygetvalues%28_,_,_%29.md)
  Fills a buffer with values from an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetvalueatindex(_:_:))*