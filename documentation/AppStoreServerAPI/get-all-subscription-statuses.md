# Get All Subscription Statuses

**Framework**: App Store Server API  
**Kind**: httpRequest

Get the statuses for all of a customer’s auto-renewable subscriptions in your app.

**Availability**:
- App Store Server API 1.0+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

This API returns the status for all of the customer’s subscriptions, organized by their subscription group identifier.

Specify multiple values for the `status` query parameter to get a response that contains subscriptions with statuses that match any of the values. For example, the following request returns subscriptions that are active ([`status`](get-all-subscription-statuses/status.md) value of `1`) and subscriptions that are in the Billing Grace Period ([`status`](get-all-subscription-statuses/status.md) value of `4`):

```javascript
GET https://api.storekit.itunes.apple.com/inApps/v1/subscriptions/{transactionId}?status=1&status=4
```

## See Also

- [object StatusResponse](statusresponse.md)
  A response that contains status information for all of a customer’s auto-renewable subscriptions in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses)*