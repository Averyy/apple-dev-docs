# CFSetGetCountOfValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of values in a set that match a given value.

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
func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> CFIndex
```

```c
extern CFIndex CFSetGetCountOfValue(CFSetRef theSet, const void *value);
```

## Return Value

The number of times `value` occurs in `theSet`. By definition, sets can not contain duplicate values, so returns `1` if `value` is contained in `theSet`, otherwise `0`.

## Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## Parameters

- `theSet`: The set to examine.
- `value`: The value for which to search in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## See Also

### Examining a Set
- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](./cfsetcontainsvalue%28_,_%29.md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](./cfsetgetcount%28_%29.md)
  Returns the number of values currently in a set.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfsetgetvalue%28_,_%29.md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfsetgetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfsetgetvalues%28_,_%29.md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetcountofvalue(_:_:))*