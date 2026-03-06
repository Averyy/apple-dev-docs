# ProfilesResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary

A response that contains a list of Profiles resources.

## Declaration

```swift
object ProfilesResponse
```

## Properties

- `data` ([Profile]) *(required)*: The resource data.
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [object Profile](profile.md)
  The data structure that represents a Profiles  resource.
- [object ProfileCreateRequest](profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](profileresponse.md)
  A response that contains a single Profiles resource.
- [object ProfilesWithoutIncludesResponse](profileswithoutincludesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/profilesresponse)*