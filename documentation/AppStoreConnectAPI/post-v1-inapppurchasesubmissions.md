# Create a review submission for an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create an In-App Purchase submission for review.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This endpoint is deprecated. Use the review submissions workflow at [Review submissions](./review-submissions.md) instead.

## Mentions

- [Managing In-App Purchases](./managing-in-app-purchases.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/inAppPurchaseSubmissions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `InAppPurchaseSubmissionCreateRequest`

## Responses

- `201` Created (`InAppPurchaseSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchasesubmissions)*