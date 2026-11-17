# ar_identifiers_enumerator_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler for enumerating a collection of identifiers.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (^)(unsigned char *) ar_identifiers_enumerator_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Discussion

> **Note**: The `identifier` will have the same lifetime as the scope of the enumerator.

## Parameters

- `identifier`: The identifier.

## See Also

### Identifier data types
- [ar_identifiers_enumerator_function_t](./ar_identifiers_enumerator_function_t.md)
  Function for enumerating a collection of identifiers.
- [ar_identifiers_t](./ar_identifiers_t.md)
  A collection of UUID identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_identifiers_enumerator_t)*