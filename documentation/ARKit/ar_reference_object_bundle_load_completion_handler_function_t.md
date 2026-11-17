# ar_reference_object_bundle_load_completion_handler_function_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Function called when a request to load a reference object from a bundle has completed.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef void (*)(void *, const char *, struct __CFBundle *, _Bool, NSObject<OS_ar_error> *, NSObject<OS_ar_reference_object> *) ar_reference_object_bundle_load_completion_handler_function_t;
```

## Parameters

- `context`: The application-defined context.
- `name`: The name of reference object that was being loaded from bundle.
- `bundle`: The bundle used for loading the reference object.
- `success`: `true` if loading succeeded, `false` otherwise.
- `error`: The error that occurred, if any.
- `reference_object`: An instance of `ar_reference_object_t` (`NULL` if loading failed). The returned object supports ARC. In non-ARC files, use `ar_release()` to release it.

## See Also

### Reference object data types
- [ar_reference_object_bundle_load_completion_handler_t](./ar_reference_object_bundle_load_completion_handler_t.md)
  Handler triggered when a request to load a reference object from a bundle has completed.
- [ar_reference_object_t](./ar_reference_object_t.md)
  Defines a physical object to detect in the environment.
- [ar_reference_object_url_load_completion_handler_function_t](./ar_reference_object_url_load_completion_handler_function_t.md)
  Function called when a request to load a reference object from a URL has completed.
- [ar_reference_object_url_load_completion_handler_t](./ar_reference_object_url_load_completion_handler_t.md)
  Handler triggered when a request to load a reference object from a URL has completed.
- [ar_reference_objects_enumerator_function_t](./ar_reference_objects_enumerator_function_t.md)
  Function for enumerating a collection of reference objects.
- [ar_reference_objects_enumerator_t](./ar_reference_objects_enumerator_t.md)
  Handler for enumerating a collection of reference objects.
- [ar_reference_objects_t](./ar_reference_objects_t.md)
  A collection of reference objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_object_bundle_load_completion_handler_function_t)*