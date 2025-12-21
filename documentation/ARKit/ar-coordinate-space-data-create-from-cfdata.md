# ar_coordinate_space_data_create_from_cfdata

**Framework**: ARKit  
**Kind**: func

Create and initialize an `ar_coordinate_space_data_t` from a `CFDataRef`.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
extern ar_coordinate_space_data_t ar_coordinate_space_data_create_from_cfdata(CFDataRef cfData);
```

#### Return Value

An instance of `ar_coordinate_space_data_t`.

#### Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## Parameters

- `cfData`: The CFDataRef object to set for the  .

## See Also

- [ar_coordinate_space_data_t](ar_coordinate_space_data_t.md)
- [ar_coordinate_space_data_copy_cfdata](ar_coordinate_space_data_copy_cfdata.md)
  Copy out a `CFDataRef` that archives the coordinate space data.
- [ar_coordinate_space_data_copy_recipient_identifers](ar_coordinate_space_data_copy_recipient_identifers.md)
  Copy the list of participant identifiers of the intended recipient for this data. Data should be broadcast if the list is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_coordinate_space_data_create_from_cfdata)*