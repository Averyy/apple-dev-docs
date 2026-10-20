# NSKeyValueChange.replacement

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Indicates that an object has been replaced in the to-many relationship that is being observed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case replacement
```

```c
NSKeyValueChangeReplacement
```

## See Also

### Constants
- [NSKeyValueChange.setting](./setting.md)
  Indicates that the value of the observed key path was set to a new value. This change can occur when observing an attribute of an object, as well as properties that specify to-one and to-many relationships.
- [NSKeyValueChange.insertion](./insertion.md)
  Indicates that an object has been inserted into the to-many relationship that is being observed.
- [NSKeyValueChange.removal](./removal.md)
  Indicates that an object has been removed from the to-many relationship that is being observed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechange/replacement)*