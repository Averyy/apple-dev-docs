# List all subscription group localizations

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all localized metadata for a specific subscription group.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This relationship is deprecated. Use [`List the localizations of a subscription group version`](./get-v1-subscriptiongroupversions-_id_-localizations.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGroups/{id}/subscriptionGroupLocalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionGroupLocalizations]` ([string]): **Allowed Values**: `name`, `customAppName`, `locale`, `state`, `subscriptionGroup`
- `fields[subscriptionGroups]` ([string]): **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`
- `include` ([string]): **Allowed Values**: `subscriptionGroup`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionGroupLocalizationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a subscription group](./post-v1-subscriptiongroups.md)
  Create a subscription group for an app.
- [List all subscription groups for an app](./get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [List subscription group IDs for an app](./get-v1-apps-_id_-relationships-subscriptiongroups.md)
- [Read subscription group information](./get-v1-subscriptiongroups-_id_.md)
  Get the details of a specific subscription group.
- [Modify a subscription group](./patch-v1-subscriptiongroups-_id_.md)
  Update the reference name for a specific subscription group.
- [Delete a subscription group](./delete-v1-subscriptiongroups-_id_.md)
  Delete a specific empty subscription group.
- [List localization IDs for a subscription group](./get-v1-subscriptiongroups-_id_-relationships-subscriptiongrouplocalizations.md)
- [List all subscriptions for a subscription group](./get-v1-subscriptiongroups-_id_-subscriptions.md)
  Get a list of all auto-renewable subscriptions in a subscription group.
- [List subscription IDs for a subscription group](./get-v1-subscriptiongroups-_id_-relationships-subscriptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongroups-_id_-subscriptiongrouplocalizations)*