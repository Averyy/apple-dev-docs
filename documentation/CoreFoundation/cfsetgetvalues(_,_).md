# CFSetGetValues(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Obtains all values in a set.

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
func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

```c
extern void CFSetGetValues(CFSetRef theSet, const void **values);
```

## Parameters

- `theSet`: The set to examine.
- `values`: A C array of pointer-sized values to be filled with values from `theSet`. The value must be a valid C array of the appropriate type and of a size at least equal to the count of `theSet`). If the values are Core Foundation objects, ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Examining a Set
- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](./cfsetcontainsvalue%28_,_%29.md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](./cfsetgetcount%28_%29.md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](./cfsetgetcountofvalue%28_,_%29.md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfsetgetvalue%28_,_%29.md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfsetgetvalueifpresent%28_,_,_%29.md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetgetvalues(_:_:))*