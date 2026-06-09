# Modify the territory availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the territory availability of a specific subscription.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities`

## See Also

- [Read the availability of a subscription](get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List the territory availability of a subscription](get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [List available territory IDs for a subscription availability](get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionavailabilities)*