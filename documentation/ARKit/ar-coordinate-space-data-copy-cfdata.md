# ar_coordinate_space_data_copy_cfdata

**Framework**: ARKit  
**Kind**: func

Copy out a `CFDataRef` that archives the coordinate space data.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern CFDataRef ar_coordinate_space_data_copy_cfdata(ar_coordinate_space_data_t data);
```

#### Return Value

The `CFDataRef`. The caller is responsible for calling `CFRelease` on the returned pointer.

## Parameters

- `data`: Coordinate space data.

## See Also

- [ar_coordinate_space_data_t](ar_coordinate_space_data_t.md)
- [ar_coordinate_space_data_copy_recipient_identifers](ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.
- [ar_coordinate_space_data_create_from_cfdata](ar_coordinate_space_data_create_from_cfdata.md)
  Create and initialize an `ar_coordinate_space_data_t` from a `CFDataRef`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_copy_cfdata)*