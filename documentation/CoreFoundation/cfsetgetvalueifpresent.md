# CFSetGetValueIfPresent(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a value is in a set, and if it exists returns the value indirectly.

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
func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

#### Return Value

`true` if `value` exists in `theSet`, otherwise `false`.

#### Discussion

This function uses the equal callback. `candidate` and all elements in the set must be understood by the equal callback. Depending on the implementation of the equal callback specified when creating `theSet`, the value returned in `value` may not have the same pointer equality as `candidate`.

## Parameters

- `theSet`: The set to examine.
- `candidate`: The value for which to search in  . Comparisons are made using the equal callback provided when   was created. If the equal callback was  , pointer equality (in C, ==) is used.
- `value`: Upon return contains the matching value if it exists in  , otherwise  . If the value is a Core Foundation object, ownership follows the  .

## See Also

- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](cfsetcontainsvalue(_:_:).md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](cfsetgetcountofvalue(_:_:).md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfsetgetvalue(_:_:).md)
  Obtains a specified value from a set.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfsetgetvalues(_:_:).md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetvalueifpresent(_:_:_:))*