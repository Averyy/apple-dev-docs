# ar_strings_enumerator_t

**Framework**: ARKit  
**Kind**: typealias

Handler for enumerating a collection of strings.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
typedef _Bool (^)(const char *) ar_strings_enumerator_t;
```

#### Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `string`: An UTF-8 encoded string representation.

## See Also

- [ar_strings_enumerator_function_t](ar_strings_enumerator_function_t.md)
  Function for enumerating a collection of strings.
- [ar_strings_t](ar_strings_t.md)
- [ar_strings_enumerate_strings](ar_strings_enumerate_strings.md)
  Enumerate a collection of strings.
- [ar_strings_enumerate_strings_f](ar_strings_enumerate_strings_f.md)
  Enumerate a collection of strings using a function.
- [ar_strings_get_count](ar_strings_get_count.md)
  Returns the number of strings in this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_strings_enumerator_t)*