# ProfilesResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

A response that contains a list of Profiles resources.

## Declaration

```
object ProfilesResponse
```

## Properties

- `data` ([Profile]) *(required)*: The resource data.
- `included` ([*]): **Allowed Types**: `BundleId`, `Device`, `Certificate`
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

### Objects
- [object Profile](./profile.md)
  The data structure that represents a Profiles  resource.
- [object ProfileCreateRequest](./profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](./profileresponse.md)
  A response that contains a single Profiles resource.
- [object ProfilesWithoutIncludesResponse](./profileswithoutincludesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/profilesresponse)*