# CFSetGetValues(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Obtains all values in a set.

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
func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theSet`: The set to examine.
- `values`: A C array of pointer-sized values to be filled with values from  . The value must be a valid C array of the appropriate type and of a size at least equal to the count of  ). If the values are Core Foundation objects, ownership follows the  .

## See Also

- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](cfsetcontainsvalue(_:_:).md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](cfsetgetcountofvalue(_:_:).md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfsetgetvalue(_:_:).md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfsetgetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetvalues(_:_:))*