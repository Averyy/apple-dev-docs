# ar_coordinate_space_data_copy_recipient_identifiers

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern ar_identifiers_tar_coordinate_space_data_copy_recipient_identifiers(ar_coordinate_space_data_t shared_coordinate_space_data);
```

#### Return Value

List the participant identifiers to which the data should be sent. Data should be broadcast to all participants if the list is empty.

#### Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## Parameters

- `shared_coordinate_space_data`: Shared coordinate space data.

## See Also

### Coordinate spaces
- [ar_coordinate_space_data_t](./ar_coordinate_space_data_t.md)
  Data for sharing coordinate space information between participants.
- [ar_coordinate_space_data_copy_cfdata](./ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_copy_recipient_identifers](./ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_create_from_cfdata](./ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` object from a `CFDataRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_copy_recipient_identifiers)*