# ar_reference_image_get_resource_group_name

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get a reference image’s resource group name.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern const char *ar_reference_image_get_resource_group_name(ar_reference_image_t reference_image);
```

## Return Value

The resource group name of the reference image, or `NULL` if it is not set. It will only be set if the reference image was loaded from a resource group.

## Discussion

> **Note**: The returned value will have the same lifetime as the input `ar_reference_image_t`.

## Parameters

- `reference_image`: The reference image.

## See Also

### Reference image functions
- [ar_reference_image_is_equal_to_reference_image](./ar_reference_image_is_equal_to_reference_image.md)
  Returns a bool value that indicates whether the two reference images are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_reference_image_get_resource_group_name)*