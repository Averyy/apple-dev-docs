# BundleIdsResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary

A response that contains a list of Bundle ID resources.

## Declaration

```swift
object BundleIdsResponse
```

## Properties

- `data` ([BundleId]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([*]): The requested relationship data.

## See Also

- [object BundleId](bundleid.md)
  The data structure that represents a Bundle IDs resource.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdResponse](bundleidresponse.md)
  A response that contains a single Bundle IDs resource.
- [object BundleIdWithoutIncludesResponse](bundleidwithoutincludesresponse.md)
  A response that contains a single Bundle IDs resource without includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/bundleidsresponse)*