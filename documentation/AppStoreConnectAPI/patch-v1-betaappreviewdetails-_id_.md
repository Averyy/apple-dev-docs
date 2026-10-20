# Modify a beta app review detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the details for a specific app’s beta app review.

**Availability**:
- App Store Connect API 1.0+

#### Overview

> ❗ **Important**:  First name, last name, phone, email cannot be cleared for the primary locale once set.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppReviewDetailUpdateRequest`

## Responses

- `200` OK (`BetaAppReviewDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betaappreviewdetails-_id_)*