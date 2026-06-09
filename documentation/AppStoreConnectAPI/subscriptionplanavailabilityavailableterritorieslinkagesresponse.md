# SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifiers of available territories for a subscription plan availability.

**Availability**:
- App Store Connect API 4.4+

## Declaration

```swift
object SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse
```

## Topics

### Dictionaries
- [object SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse.Data](subscriptionplanavailabilityavailableterritorieslinkagesresponse/data-data.dictionary.md)
  The data element of the response body.

## Properties

- `data` ([SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object SubscriptionPlanAvailability](subscriptionplanavailability.md)
  A configuration object for a subscription’s plan availability, specifying the plan type, the territories in which it is available, and whether it’s automatically available in new territories.
- [object SubscriptionPlanAvailabilityCreateRequest](subscriptionplanavailabilitycreaterequest.md)
  The request body you use to create a subscription plan availability.
- [object SubscriptionPlanAvailabilityUpdateRequest](subscriptionplanavailabilityupdaterequest.md)
  The request body you use to modify a subscription plan availability.
- [object SubscriptionPlanAvailabilityResponse](subscriptionplanavailabilityresponse.md)
  The response body for endpoints that create or read a single subscription plan availability.
- [object SubscriptionPlanAvailabilitiesResponse](subscriptionplanavailabilitiesresponse.md)
  The response body for endpoints that list subscription plan availabilities.
- [object SubscriptionPlanAvailabilitiesLinkagesResponse](subscriptionplanavailabilitieslinkagesresponse.md)
  A response containing the resource identifiers of subscription plan availabilities.
- [object SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesRequest](subscriptionplanavailabilityavailableterritorieslinkagesrequest.md)
  A request body you use to replace the available territories for a subscription plan availability.
- [type SubscriptionPlanType](subscriptionplantype.md)
  A string that indicates the billing plan type for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionplanavailabilityavailableterritorieslinkagesresponse)*