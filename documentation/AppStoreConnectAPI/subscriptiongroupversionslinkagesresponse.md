# SubscriptionGroupVersionsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response with the related resource identifiers for the versions of a subscription group.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionGroupVersionsLinkagesResponse
```

## Topics

### Dictionaries
- [object SubscriptionGroupVersionsLinkagesResponse.Data](subscriptiongroupversionslinkagesresponse/data-data.dictionary.md)
  The data element of the response body.

## Properties

- `data` ([SubscriptionGroupVersionsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object SubscriptionGroupVersion](subscriptiongroupversion.md)
  A draft version of a subscription group that captures its localized metadata for App Review submission.
- [object SubscriptionGroupVersionCreateRequest](subscriptiongroupversioncreaterequest.md)
  The request body you use to create a draft version of a subscription group.
- [object SubscriptionGroupVersionLocalizationsLinkagesResponse](subscriptiongroupversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription group version’s localizations.
- [object SubscriptionGroupVersionResponse](subscriptiongroupversionresponse.md)
  The response body for endpoints that create or read a subscription group version.
- [object SubscriptionGroupVersionsResponse](subscriptiongroupversionsresponse.md)
  The response body for endpoints that list subscription group versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupversionslinkagesresponse)*