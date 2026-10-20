# ProfileResponse

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

A response that contains a single Profiles resource.

## Declaration

```
object ProfileResponse
```

## Properties

- `data` (Profile) *(required)*: The resource data.
- `included` ([*]): **Allowed Types**: `BundleId`, `Device`, `Certificate`
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects
- [object Profile](./profile.md)
  The data structure that represents a Profiles  resource.
- [object ProfileCreateRequest](./profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfilesResponse](./profilesresponse.md)
  A response that contains a list of Profiles resources.
- [object ProfilesWithoutIncludesResponse](./profileswithoutincludesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/profileresponse)*