# CFSetContainsValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean that indicates whether a set contains a given value.

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
func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> Bool
```

```c
extern Boolean CFSetContainsValue(CFSetRef theSet, const void *value);
```

## Return Value

`true` if `value` is contained in `theSet`, otherwise `false`.

## Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## Parameters

- `theSet`: The set to search.
- `value`: The value to match in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## See Also

### Examining a Set
- [func CFSetGetCount(CFSet!) -> CFIndex](./cfsetgetcount%28_%29.md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](./cfsetgetcountofvalue%28_,_%29.md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfsetgetvalue%28_,_%29.md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfsetgetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfsetgetvalues%28_,_%29.md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcontainsvalue(_:_:))*