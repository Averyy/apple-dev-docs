# NominationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of app nominations submitted for App Store editorial featuring consideration.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object NominationsResponse
```

## Properties

- `data` ([Nomination]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Nomination](nomination.md)
  A developer recommendation submitted to Apple proposing an app or in-app event for App Store editorial featuring.
- [object NominationUpdateRequest](nominationupdaterequest.md)
  The request body you use to update a featuring nomination.
- [object NominationCreateRequest](nominationcreaterequest.md)
  The request body you use to create a featuring nomination.
- [object NominationResponse](nominationresponse.md)
  A response containing a single App Store nomination submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/nominationsresponse)*