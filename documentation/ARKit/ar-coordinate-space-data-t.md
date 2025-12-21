# ar_coordinate_space_data_t

**Framework**: ARKit  
**Kind**: typealias

**Availability**:
- visionOS 26.0+

## Declaration

```swift
typedef NSObject<OS_ar_coordinate_space_data> * ar_coordinate_space_data_t;
```

## See Also

- [ar_coordinate_space_data_copy_cfdata](ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_copy_recipient_identifers](ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_create_from_cfdata](ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` from a `CFDataRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_t)*