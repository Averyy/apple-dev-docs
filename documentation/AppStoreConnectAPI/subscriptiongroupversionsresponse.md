# SubscriptionGroupVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list subscription group versions.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```
object SubscriptionGroupVersionsResponse
```

## Properties

- `data` ([SubscriptionGroupVersion]) *(required)*
- `included` ([*]): **Allowed Types**: `SubscriptionGroupLocalizationV2`, `SubscriptionGroup`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object SubscriptionGroupVersion](./subscriptiongroupversion.md)
  A draft version of a subscription group that captures its localized metadata for App Review submission.
- [object SubscriptionGroupVersionCreateRequest](./subscriptiongroupversioncreaterequest.md)
  The request body you use to create a draft version of a subscription group.
- [object SubscriptionGroupVersionLocalizationsLinkagesResponse](./subscriptiongroupversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription group version’s localizations.
- [object SubscriptionGroupVersionResponse](./subscriptiongroupversionresponse.md)
  The response body for endpoints that create or read a subscription group version.
- [object SubscriptionGroupVersionsLinkagesResponse](./subscriptiongroupversionslinkagesresponse.md)
  A response with the related resource identifiers for the versions of a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupversionsresponse)*