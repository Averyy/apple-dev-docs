# ar_reference_object_is_equal_to_reference_object

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two reference objects are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_reference_object_is_equal_to_reference_object(ar_reference_object_t reference_object, ar_reference_object_t other_reference_object);
```

## Return Value

`YES` if the reference objects are equal, otherwise `NO`.

## Parameters

- `reference_object`: A reference object to be compared.
- `other_reference_object`: The other reference object to be compared to.

## See Also

### Reference object functions
- [ar_reference_object_get_identifier](./ar_reference_object_get_identifier.md)
  Get identifier for the reference object.
- [ar_reference_object_get_input_file_path](./ar_reference_object_get_input_file_path.md)
  Get the input file path used to load the reference object.
- [ar_reference_object_get_name](./ar_reference_object_get_name.md)
  Get a reference object’s name.
- [ar_reference_object_get_usdz_file_path](./ar_reference_object_get_usdz_file_path.md)
  Get path to a copy of the USDZ file for the object, if the object has one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_object_is_equal_to_reference_object)*