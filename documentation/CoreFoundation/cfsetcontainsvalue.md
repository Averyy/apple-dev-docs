# CFSetContainsValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean that indicates whether a set contains a given value.

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
func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> Bool
```

#### Return Value

`true` if `value` is contained in `theSet`, otherwise `false`.

#### Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## Parameters

- `theSet`: The set to search.
- `value`: The value to match in  . Comparisons are made using the equal callback provided when   was created. If the equal callback was  , pointer equality (in C, ==) is used.

## See Also

- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](cfsetgetcountofvalue(_:_:).md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfsetgetvalue(_:_:).md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfsetgetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfsetgetvalues(_:_:).md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcontainsvalue(_:_:))*