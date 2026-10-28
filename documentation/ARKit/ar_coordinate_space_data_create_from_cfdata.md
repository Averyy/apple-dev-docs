# ar_coordinate_space_data_create_from_cfdata

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Create and initialize an `ar_coordinate_space_data_t` object from a `CFDataRef`.

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern ar_coordinate_space_data_tar_coordinate_space_data_create_from_cfdata(CFDataRef cfData);
```

## Return Value

An instance of `ar_coordinate_space_data_t`.

## Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## Parameters

- `cfData`: The `CFDataRef` object to set for the `ar_coordinate_space_data_t`.

## See Also

### Coordinate spaces
- [ar_coordinate_space_data_t](./ar_coordinate_space_data_t.md)
  Data for sharing coordinate space information between participants.
- [ar_coordinate_space_data_copy_cfdata](./ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_copy_recipient_identifers](./ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_copy_recipient_identifiers](./ar_coordinate_space_data_copy_recipient_identifiers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_create_from_cfdata)*