# ar_identifiers_enumerator_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function for enumerating a collection of identifiers.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (*)(void *, unsigned char *) ar_identifiers_enumerator_function_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `context`: The application-defined context.
- `identifier`: The identifier.

## See Also

### Identifier data types
- [ar_identifiers_enumerator_t](./ar_identifiers_enumerator_t.md)
  Handler for enumerating a collection of identifiers.
- [ar_identifiers_t](./ar_identifiers_t.md)
  A collection of UUID identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_identifiers_enumerator_function_t)*