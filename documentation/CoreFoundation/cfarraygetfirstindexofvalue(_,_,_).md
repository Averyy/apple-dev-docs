# CFArrayGetFirstIndexOfValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Searches an array forward for a value.

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
func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex
```

```c
extern CFIndex CFArrayGetFirstIndexOfValue(CFArrayRef theArray, CFRange range, const void *value);
```

## Return Value

The lowest index of the matching values in the range, or `-1` if no value in the range matched.

## Parameters

- `theArray`: The array to examine.
- `range`: The range within `theArray` to search. The range must lie within the bounds of  `theArray`. The range may be empty (length `0`). The search progresses from the lowest index defined by the range to the highest.
- `value`: The value for which to find a match in `theArray`. The equal callback provided when `theArray` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theArray`, is not understood by the equal callback, the behavior is undefined.

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
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetlastindexofvalue%28_,_,_%29.md)
  Searches an array backward for a value.
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfarraygetvalues%28_,_,_%29.md)
  Fills a buffer with values from an array.
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](./cfarraygetvalueatindex%28_,_%29.md)
  Retrieves a value at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetfirstindexofvalue(_:_:_:))*