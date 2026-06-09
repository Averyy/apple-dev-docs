# Nomination

**Framework**: App Store Connect API  
**Kind**: dictionary

A developer recommendation submitted to Apple proposing an app or in-app event for App Store editorial featuring.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object Nomination
```

## Topics

### Dictionaries
- [object Nomination.Attributes](nomination/attributes-data.dictionary.md)
- [object Nomination.Relationships](nomination/relationships-data.dictionary.md)

## Properties

- `attributes` (Nomination.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (Nomination.Relationships)
- `type` (string) *(required)*

## See Also

- [object NominationUpdateRequest](nominationupdaterequest.md)
  The request body you use to update a featuring nomination.
- [object NominationCreateRequest](nominationcreaterequest.md)
  The request body you use to create a featuring nomination.
- [object NominationResponse](nominationresponse.md)
  A response containing a single App Store nomination submission.
- [object NominationsResponse](nominationsresponse.md)
  A response containing a list of app nominations submitted for App Store editorial featuring consideration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/nomination)*