# propertyType()

**Framework**: Address Book  
**Kind**: method

Returns the type for the values in a multivalue list.

**Availability**:
- macOS ?+

## Declaration

```swift
func propertyType() -> ABPropertyType
```

#### Discussion

If the multivalue list is empty or its values are of different types, it returns `kABErrorInProperty`.

## See Also

- [func count() -> Int](abmultivalue/count.md)
  Returns the number of entries in a multivalue list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/propertytype())*