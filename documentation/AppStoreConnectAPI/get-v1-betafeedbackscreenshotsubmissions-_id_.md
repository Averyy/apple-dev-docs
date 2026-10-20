# Read a Beta Feedback Screenshot Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific beta feedback screenshot submission.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaFeedbackScreenshotSubmissions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackScreenshotSubmissions` resource ID from the [`List All Beta Feedback Screenshot Submissions for an App`](./get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md) response.

### Query Parameters

- `fields[betaFeedbackScreenshotSubmissions]` ([string]): **Allowed Values**: `createdDate`, `comment`, `email`, `deviceModel`, `osVersion`, `locale`, `timeZone`, `architecture`, `connectionType`, `pairedAppleWatch`, `appUptimeInMilliseconds`, `diskBytesAvailable`, `diskBytesTotal`, `batteryPercentage`, `screenWidthInPoints`, `screenHeightInPoints`, `appPlatform`, `devicePlatform`, `deviceFamily`, `buildBundleId`, `screenshots`, `build`, `tester`
- `include` ([string]): **Allowed Values**: `build`, `tester`
- `fields[betaTesters]` ([string]): **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`

## Responses

- `200` OK (`BetaFeedbackScreenshotSubmissionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and deleting beta feedback screenshot submissions
- [List All Beta Feedback Screenshot Submissions for an App](./get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
- [List all beta feedback screenshot submission ids for an app](./get-v1-apps-_id_-relationships-betafeedbackscreenshotsubmissions.md)
  Get a list of beta feedback screenshot submissions for a specific app.
- [Delete a Beta Feedback Screenshot Submission](./delete-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Delete a beta feedback screenshot submission from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betafeedbackscreenshotsubmissions-_id_)*