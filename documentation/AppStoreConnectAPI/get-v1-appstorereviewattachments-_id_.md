# Read app store review attachment information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about an App Store review attachment and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store review attachment resource ID from the [`List all review attachments for an app store review detail`](./get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md) response.

### Query Parameters

- `fields[appStoreReviewAttachments]` ([string]): Additional fields to include for each App Store review attachment resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreReviewDetail`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appStoreReviewDetail`
- `fields[appStoreReviewDetails]` ([string]): **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`

## Responses

- `200` OK (`AppStoreReviewAttachmentResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Attachment Information
- [List all review attachments for an app store review detail](./get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md)
  List all the App Store review attachments you include with a version when you submit it for App Review.
- [List App Store review attachment IDs for an App Store review detail](./get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstorereviewattachments-_id_)*