# CFSetGetValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Obtains a specified value from a set.

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
func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer!
```

```c
extern const void *CFSetGetValue(CFSetRef theSet, const void *value);
```

## Return Value

A pointer to the requested value, or `NULL` if the value is not in `theSet`. If the value is a Core Foundation object, Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Since this function uses the equal callback, `value` all elements in the set must be understood by the equal callback. Depending on the implementation of the equal callback specified when creating `theSet`, the value returned may not have the same pointer equality as `value`.

## Parameters

- `theSet`: The set to examine.
- `value`: The value for which to search in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## See Also

### Examining a Set
- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](./cfsetcontainsvalue%28_,_%29.md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](./cfsetgetcount%28_%29.md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](./cfsetgetcountofvalue%28_,_%29.md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfsetgetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfsetgetvalues%28_,_%29.md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetvalue(_:_:))*