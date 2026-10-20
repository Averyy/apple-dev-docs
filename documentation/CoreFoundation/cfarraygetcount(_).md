# CFArrayGetCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of values currently in an array.

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
func CFArrayGetCount(_ theArray: CFArray!) -> CFIndex
```

```c
extern CFIndex CFArrayGetCount(CFArrayRef theArray);
```

#### Return Value

The number of values in `theArray`.

## Parameters

- `theArray`: The array to examine.

## See Also

### Examining an Array
- [func CFArrayBSearchValues(CFArray!, CFRange, UnsafeRawPointer!, CFComparatorFunction!, UnsafeMutableRawPointer!) -> CFIndex](./cfarraybsearchvalues%28_,_,_,_,_%29.md)
  Searches an array for a value using a binary search algorithm.
- [func CFArrayContainsValue(CFArray!, CFRange, UnsafeRawPointer!) -> Bool](./cfarraycontainsvalue%28_,_,_%29.md)
  Reports whether or not a value is in an array.
- [func CFArrayGetCountOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetcountofvalue%28_,_,_%29.md)
  Counts the number of times a given value occurs in an array.
- [func CFArrayGetFirstIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetfirstindexofvalue%28_,_,_%29.md)
  Searches an array forward for a value.
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](./cfarraygetlastindexofvalue%28_,_,_%29.md)
  Searches an array backward for a value.
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfarraygetvalues%28_,_,_%29.md)
  Fills a buffer with values from an array.
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](./cfarraygetvalueatindex%28_,_%29.md)
  Retrieves a value at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygetcount(_:))*