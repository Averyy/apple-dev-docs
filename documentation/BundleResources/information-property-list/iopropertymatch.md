# IOPropertyMatch

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The device-specific keys the system must match in order to use your driver.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `IOPropertyMatch`
- **Type**: dictionary

## Discussion

The value of this key is a dictionary of device-specific keys and values to use during the matching process. For the system to match the driver personality to a device, all keys in the dictionary must be present in the device, and all values must exactly match the device-provided values.

## See Also

### Advanced Match Criteria
- [IONameMatch](./ionamematch.md)
  One or more strings that contain the names of possible provider objects in the system registry.
- [IOResourceMatch](./ioresourcematch.md)
  One or more system-specific or device-specific resources that your driver requires.
- [IOParentMatch](./ioparentmatch.md)
- [IOPathMatch](./iopathmatch.md)
- [IOMatchCategory](./iomatchcategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iopropertymatch)*