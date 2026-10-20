# CFSetGetCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of values currently in a set.

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
func CFSetGetCount(_ theSet: CFSet!) -> CFIndex
```

```c
extern CFIndex CFSetGetCount(CFSetRef theSet);
```

#### Return Value

The number of values in `theSet`.

## Parameters

- `theSet`: The set to examine.

## See Also

### Examining a Set
- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](./cfsetcontainsvalue%28_,_%29.md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](./cfsetgetcountofvalue%28_,_%29.md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfsetgetvalue%28_,_%29.md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfsetgetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfsetgetvalues%28_,_%29.md)
  Obtains all values in a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetcount(_:))*