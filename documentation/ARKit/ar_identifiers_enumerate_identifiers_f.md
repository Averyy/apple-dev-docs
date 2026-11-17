# ar_identifiers_enumerate_identifiers_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates a collection of identifiers using a function.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_identifiers_enumerate_identifiers_f(ar_identifiers_t identifiers, void *context, ar_identifiers_enumerator_function_t identifiers_enumerator_function);
```

## Parameters

- `identifiers`: The collection of identifiers.
- `context`: The application-defined context parameter to pass to the function.
- `identifiers_enumerator_function`: The enumerator function.

## See Also

### Identifier functions
- [ar_identifiers_enumerate_identifiers](./ar_identifiers_enumerate_identifiers.md)
  Enumerate a collection of identifiers.
- [ar_identifiers_get_count](./ar_identifiers_get_count.md)
  Get the count of identifiers in a collection.
- [ar_identifiers_is_equal_to_identifiers](./ar_identifiers_is_equal_to_identifiers.md)
  Returns a bool value that indicates whether the two collections of identifiers are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_identifiers_enumerate_identifiers_f)*