# CFSetGetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Obtains a specified value from a set.

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
func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer!
```

#### Return Value

A pointer to the requested value, or `NULL` if the value is not in `theSet`. If the value is a Core Foundation object, Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

Since this function uses the equal callback, `value` all elements in the set must be understood by the equal callback. Depending on the implementation of the equal callback specified when creating `theSet`, the value returned may not have the same pointer equality as `value`.

## Parameters

- `theSet`: The set to examine.
- `value`: The value for which to search in  . Comparisons are made using the equal callback provided when   was created. If the equal callback was  , pointer equality (in C, ==) is used.

## See Also

- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](cfsetcontainsvalue(_:_:).md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](cfsetgetcountofvalue(_:_:).md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfsetgetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfsetgetvalues(_:_:).md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetvalue(_:_:))*