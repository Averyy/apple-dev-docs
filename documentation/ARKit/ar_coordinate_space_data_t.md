# ar_coordinate_space_data_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Data for sharing coordinate space information between participants.

**Availability**:
- visionOS 26.0+

## Declaration

```c
typedef NSObject<OS_ar_coordinate_space_data> * ar_coordinate_space_data_t;
```

## See Also

### Coordinate spaces
- [ar_coordinate_space_data_copy_cfdata](./ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_copy_recipient_identifers](./ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_create_from_cfdata](./ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` object from a `CFDataRef`.
- [ar_coordinate_space_data_copy_recipient_identifiers](./ar_coordinate_space_data_copy_recipient_identifiers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_t)*