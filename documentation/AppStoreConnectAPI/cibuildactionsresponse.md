# CiBuildActionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Build Actions resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildActionsResponse
```

## Properties

- `data` ([CiBuildAction]) *(required)*: The resource data.
- `included` ([CiBuildRun]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object CiBuildRun](cibuildrun.md)
  The data structure that represents a Build Runs resource.
- [object CiBuildRunCreateRequest](cibuildruncreaterequest.md)
  The request body you use to start a new Xcode Cloud build.
- [object CiBuildRunResponse](cibuildrunresponse.md)
  A response that contains a single Build Runs resource.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildactionsresponse)*