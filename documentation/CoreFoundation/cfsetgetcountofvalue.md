# CFSetGetCountOfValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of values in a set that match a given value.

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
func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> CFIndex
```

#### Return Value

The number of times `value` occurs in `theSet`. By definition, sets can not contain duplicate values, so returns `1` if `value` is contained in `theSet`, otherwise `0`.

#### Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## Parameters

- `theSet`: The set to examine.
- `value`: The value for which to search in  . Comparisons are made using the equal callback provided when   was created. If the equal callback was  , pointer equality (in C, ==) is used.

## See Also

- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](cfsetcontainsvalue(_:_:).md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfsetgetvalue(_:_:).md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfsetgetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfsetgetvalues(_:_:).md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetcountofvalue(_:_:))*