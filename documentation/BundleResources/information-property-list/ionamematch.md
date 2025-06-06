# IONameMatch

**Framework**: Bundle Resources  
**Kind**: typealias

One or more strings that contain the names of possible provider objects in the system registry.

**Availability**:
- macOS 10.0+

#### Discussion

The value of this key is a string or an array of strings. The system begins the matching process with a provider object, and looks for additional drivers or nubs that support that provider object. When this key is present, the system compares its values to the provider object’s name. (It also compares the strings to the provider’s `compatible` and `device_type` properties.) If it doesn’t find any matches, the system doesn’t match the driver to the provider object.

The default name of a provider object is its class name, but providers may register a custom name. For more information about how to set or get information for registered services, see [`IORegistryEntry`](https://developer.apple.com/documentation/kernel/ioregistryentry).

## See Also

- [IOPropertyMatch](information-property-list/iopropertymatch.md)
  The device-specific keys the system must match in order to use your driver.
- [IOResourceMatch](information-property-list/ioresourcematch.md)
  One or more system-specific or device-specific resources that your driver requires.
- [IOParentMatch](information-property-list/ioparentmatch.md)
- [IOPathMatch](information-property-list/iopathmatch.md)
- [IOMatchCategory](information-property-list/iomatchcategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ionamematch)*