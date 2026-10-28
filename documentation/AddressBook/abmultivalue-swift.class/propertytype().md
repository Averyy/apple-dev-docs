# propertyType()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the type for the values in a multivalue list.

**Availability**:
- macOS

## Declaration

```swift
func propertyType() -> ABPropertyType
```

```objc
- (ABPropertyType) propertyType;
```

## Discussion

If the multivalue list is empty or its values are of different types, it returns `kABErrorInProperty`.

## See Also

### Querying the list
- [func count() -> Int](./count%28%29.md)
  Returns the number of entries in a multivalue list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/propertytype())*