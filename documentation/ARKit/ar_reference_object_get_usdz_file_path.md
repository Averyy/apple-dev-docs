# ar_reference_object_get_usdz_file_path

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get path to a copy of the USDZ file for the object, if the object has one.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern CFURLRefar_reference_object_get_usdz_file_path(ar_reference_object_t reference_object);
```

## Return Value

The path to the USDZ file.

## Discussion

> **Note**: The returned value will have the same lifetime as the `ar_reference_object_t`.

## Parameters

- `reference_object`: Reference object.

## See Also

### Reference object functions
- [ar_reference_object_get_identifier](./ar_reference_object_get_identifier.md)
  Get identifier for the reference object.
- [ar_reference_object_get_input_file_path](./ar_reference_object_get_input_file_path.md)
  Get the input file path used to load the reference object.
- [ar_reference_object_get_name](./ar_reference_object_get_name.md)
  Get a reference object’s name.
- [ar_reference_object_is_equal_to_reference_object](./ar_reference_object_is_equal_to_reference_object.md)
  Returns a bool value that indicates whether the two reference objects are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_object_get_usdz_file_path)*