# IOResourceMatch

**Framework**: Bundle Resources  
**Kind**: typealias

One or more system-specific or device-specific resources that your driver requires.

**Availability**:
- macOS 10.0+

#### Discussion

The value of this key is a string or an array of strings. Each string contains the name of a resource that must be published in the global resource list before the system loads the driver. For example, specify `IOBSD` to prevent the system from loading your driver until after the BSD kernel is available.

To access the list of global resources, call the [`getResourceService`](https://developer.apple.com/documentation/kernel/ioservice/1532617-getresourceservice) method of [`IOService`](https://developer.apple.comhttps://developer.apple.com/documentation/kernel/ioservice-1g). To publish custom resources from your driver, call the [`publishResource`](https://developer.apple.com/documentation/kernel/ioservice/1532848-publishresource) method.

## See Also

- [IOPropertyMatch](information-property-list/iopropertymatch.md)
  The device-specific keys the system must match in order to use your driver.
- [IONameMatch](information-property-list/ionamematch.md)
  One or more strings that contain the names of possible provider objects in the system registry.
- [IOParentMatch](information-property-list/ioparentmatch.md)
- [IOPathMatch](information-property-list/iopathmatch.md)
- [IOMatchCategory](information-property-list/iomatchcategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioresourcematch)*