# ar_reference_image_is_equal_to_reference_image

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two reference images are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_reference_image_is_equal_to_reference_image(ar_reference_image_t reference_image, ar_reference_image_t other_reference_image);
```

## Return Value

`YES` if the reference images are equal, otherwise `NO`.

## Parameters

- `reference_image`: A reference image to be compared.
- `other_reference_image`: The other reference image to be compared to.

## See Also

### Reference image functions
- [ar_reference_image_get_resource_group_name](./ar_reference_image_get_resource_group_name.md)
  Get a reference image’s resource group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_image_is_equal_to_reference_image)*