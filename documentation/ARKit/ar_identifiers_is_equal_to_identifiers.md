# ar_identifiers_is_equal_to_identifiers

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two collections of identifiers are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_identifiers_is_equal_to_identifiers(ar_identifiers_t identifiers, ar_identifiers_t other_identifiers);
```

## Return Value

YES if the collections of identifiers are equal, otherwise NO.

## Parameters

- `identifiers`: A collection of identifiers to be compared.
- `other_identifiers`: The other collection of identifiers to be compared to.

## See Also

### Identifier functions
- [ar_identifiers_enumerate_identifiers](./ar_identifiers_enumerate_identifiers.md)
  Enumerate a collection of identifiers.
- [ar_identifiers_enumerate_identifiers_f](./ar_identifiers_enumerate_identifiers_f.md)
  Enumerates a collection of identifiers using a function.
- [ar_identifiers_get_count](./ar_identifiers_get_count.md)
  Get the count of identifiers in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_identifiers_is_equal_to_identifiers)*