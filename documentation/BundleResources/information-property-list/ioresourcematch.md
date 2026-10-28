# IOResourceMatch

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

One or more system-specific or device-specific resources that your driver requires.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `IOResourceMatch`
- **Type**: string

## Discussion

The value of this key is a string or an array of strings. Each string contains the name of a resource that must be published in the global resource list before the system loads the driver. For example, specify `IOBSD` to prevent the system from loading your driver until after the BSD kernel is available.

To access the list of global resources, call the [`getResourceService`](../../kernel/ioservice/api-1532617-getresourceservice.md) method of [IOService](../../kernel/ioservice.md). To publish custom resources from your driver, call the [`publishResource`](../../kernel/ioservice/api-1532848-publishresource.md) method.

## See Also

### Advanced Match Criteria
- [IOPropertyMatch](./iopropertymatch.md)
  The device-specific keys the system must match in order to use your driver.
- [IONameMatch](./ionamematch.md)
  One or more strings that contain the names of possible provider objects in the system registry.
- [IOParentMatch](./ioparentmatch.md)
- [IOPathMatch](./iopathmatch.md)
- [IOMatchCategory](./iomatchcategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioresourcematch)*