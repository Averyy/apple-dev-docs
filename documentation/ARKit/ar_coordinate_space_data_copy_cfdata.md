# ar_coordinate_space_data_copy_cfdata

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Copy out a `CFDataRef` that archives the coordinate space data.

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern CFDataRefar_coordinate_space_data_copy_cfdata(ar_coordinate_space_data_t data);
```

#### Return Value

The `CFDataRef`. The caller is responsible for calling `CFRelease` on the returned pointer.

## Parameters

- `data`: Coordinate space data.

## See Also

### Coordinate spaces
- [ar_coordinate_space_data_t](./ar_coordinate_space_data_t.md)
  Data for sharing coordinate space information between participants.
- [ar_coordinate_space_data_copy_recipient_identifers](./ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_create_from_cfdata](./ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` object from a `CFDataRef`.
- [ar_coordinate_space_data_copy_recipient_identifiers](./ar_coordinate_space_data_copy_recipient_identifiers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_copy_cfdata)*