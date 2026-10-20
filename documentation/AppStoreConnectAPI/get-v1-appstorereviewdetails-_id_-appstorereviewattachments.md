# List all review attachments for an app store review detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all the App Store review attachments you include with a version when you submit it for App Review.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreReviewDetails/{id}/appStoreReviewAttachments`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review detail resource ID from the [`Read the app store review details resource information of an app store version`](./get-v1-appstoreversions-_id_-appstorereviewdetail.md) response.

### Query Parameters

- `fields[appStoreReviewAttachments]` ([string]): Additional fields to include for each App Store review attachment resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreReviewDetail`
- `limit` (integer): The maximum number of App Store review attachment resources to return.

  **Maximum**: `200`
- `fields[appStoreReviewDetails]` ([string]): Additional fields to include for each App Store review detail resource returned by the response.

  **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreReviewDetail`

## Responses

- `200` OK (`AppStoreReviewAttachmentsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Attachment Information
- [Read app store review attachment information](./get-v1-appstorereviewattachments-_id_.md)
  Get information about an App Store review attachment and its upload and processing status.
- [List App Store review attachment IDs for an App Store review detail](./get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstorereviewdetails-_id_-appstorereviewattachments)*