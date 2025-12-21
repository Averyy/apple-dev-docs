# ar_strings_enumerate_strings_f

**Framework**: ARKit  
**Kind**: func

Enumerate a collection of strings using a function.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern void ar_strings_enumerate_strings_f(ar_strings_t strings, void * context, ar_strings_enumerator_function_t strings_enumerator_function);
```

## Parameters

- `strings`: Strings collection.
- `context`: The application-defined context parameter to pass to the function.
- `strings_enumerator_function`: The enumerator handler.

## See Also

- [ar_strings_enumerator_function_t](ar_strings_enumerator_function_t.md)
  Function for enumerating a collection of strings.
- [ar_strings_enumerator_t](ar_strings_enumerator_t.md)
  Handler for enumerating a collection of strings.
- [ar_strings_t](ar_strings_t.md)
- [ar_strings_enumerate_strings](ar_strings_enumerate_strings.md)
  Enumerate a collection of strings.
- [ar_strings_get_count](ar_strings_get_count.md)
  Returns the number of strings in this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_strings_enumerate_strings_f)*