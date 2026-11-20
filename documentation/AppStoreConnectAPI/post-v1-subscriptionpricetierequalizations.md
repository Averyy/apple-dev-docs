# Create a subscription price tier equalization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Calculate equalized volume pricing tiers for every territory from a base territory’s tiers.

**Availability**:
- App Store Connect API 4.6.1+

## Mentions

- [App Store Connect API 4.6.1 release notes](./app-store-connect-api-4-6-1-release-notes.md)
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionPriceTierEqualizations`

## Parameters

### Query Parameters

- `fields[subscriptionPricePoints]` ([string]): Additional fields to include for each subscription price points resource returned by the response.

  **Allowed Values**: `customerPrice`, `proceeds`, `proceedsYear2`, `territory`, `equalizations`, `adjustedEqualizations`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `priceTierPricePoints`
- `limit[priceTierPricePoints]` (integer): The maximum number of related price tier price points resources to return.

  **Maximum**: `50`
- `fields[subscriptionPriceTierEqualizations]` ([string]): Additional fields to include for each subscription price tier equalizations resource returned by the response.

  **Allowed Values**: `equalizedPrices`, `priceTierPricePoints`

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPriceTierEqualizationCreateRequest`

The request body you use to create a subscription price tier equalization.

## Responses

- `201` Created (`SubscriptionPriceTierEqualizationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionpricetierequalizations)*