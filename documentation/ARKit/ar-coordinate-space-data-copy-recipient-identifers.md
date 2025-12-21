# ar_coordinate_space_data_copy_recipient_identifers

**Framework**: ARKit  
**Kind**: func

Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern ar_identifiers_t ar_coordinate_space_data_copy_recipient_identifers(ar_coordinate_space_data_t shared_coordinate_space_data);
```

#### Return Value

List the participant identifiers to which the data should be sent. Data should be broadcast to all participants if the list is empty.

#### Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## Parameters

- `shared_coordinate_space_data`: Shared coordinate space data.

## See Also

- [ar_coordinate_space_data_t](ar_coordinate_space_data_t.md)
- [ar_coordinate_space_data_copy_cfdata](ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_create_from_cfdata](ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` from a `CFDataRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_copy_recipient_identifers)*