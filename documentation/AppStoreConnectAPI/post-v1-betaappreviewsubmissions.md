# Submit an app for beta review

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Submit an app for beta app review to allow external testing.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [Uploading and versioning Apple hosted background assets](./managing-apple-hosted-background-assets.md)

## Overview

> ❗ **Important**:  Before submitting to beta app review, you need to add a description for all `betaAppLocalizations`. To add a description, use [`Modify a beta app localization`](./patch-v1-betaapplocalizations-_id_.md).

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaAppReviewSubmissions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppReviewSubmissionCreateRequest`

## Responses

- `201` Created (`BetaAppReviewSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betaappreviewsubmissions)*