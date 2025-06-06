# CFArrayBSearchValues(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Searches an array for a value using a binary search algorithm.

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
func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutableRawPointer!) -> CFIndex
```

#### Return Value

The return value is one of the following:

#### Discussion

- The index of a value that matched, if the target value matches one or more in the range.
- Greater than or equal to the end point of the range, if the value is greater than all the values in the range.
- The index of the value greater than the target value, if the value lies between two of (or less than all of) the values in the range.

## Parameters

- `theArray`: An array, sorted from least to greatest according to the   function.
- `range`: The range within   to search. The range must not exceed the bounds of  . The range may be empty (length  ).
- `value`: The value for which to find a match in  . If  , or any other value in  , is not understood by the   callback, the behavior is undefined.
- `comparator`: The function with the comparator function type signature that is used in the binary search operation to compare values in   with the given value. If there are values in the range that the   function does not expect or cannot properly compare, the behavior is undefined.
- `context`: A pointer-sized program-defined value, which is passed as the third argument to the   function, but is otherwise unused by this function. If the context is not what is expected by the   function, the behavior is undefined.

## See Also

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
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](cfarraygetvalueatindex(_:_:).md)
  Retrieves a value at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraybsearchvalues(_:_:_:_:_:))*