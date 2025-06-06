# CFArrayGetFirstIndexOfValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Searches an array forward for a value.

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
func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex
```

#### Return Value

The lowest index of the matching values in the range, or `-1` if no value in the range matched.

## Parameters

- `theArray`: The array to examine.
- `range`: The range within   to search. The range must lie within the bounds of   . The range may be empty (length  ). The search progresses from the lowest index defined by the range to the highest.
- `value`: The value for which to find a match in  . The equal callback provided when   was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in  , is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFArrayBSearchValues(CFArray!, CFRange, UnsafeRawPointer!, CFComparatorFunction!, UnsafeMutableRawPointer!) -> CFIndex](cfarraybsearchvalues(_:_:_:_:_:).md)
  Searches an array for a value using a binary search algorithm.
- [func CFArrayContainsValue(CFArray!, CFRange, UnsafeRawPointer!) -> Bool](cfarraycontainsvalue(_:_:_:).md)
  Reports whether or not a value is in an array.
- [func CFArrayGetCount(CFArray!) -> CFIndex](cfarraygetcount(_:).md)
  Returns the number of values currently in an array.
- [func CFArrayGetCountOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetcountofvalue(_:_:_:).md)
  Counts the number of times a given value occurs in an array.
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetlastindexofvalue(_:_:_:).md)
  Searches an array backward for a value.
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfarraygetvalues(_:_:_:).md)
  Fills a buffer with values from an array.
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](cfarraygetvalueatindex(_:_:).md)
  Retrieves a value at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetfirstindexofvalue(_:_:_:))*