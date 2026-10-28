# Read the beta app review details resource of an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the beta app review details for a specific app.

**Availability**:
- App Store Connect API 1.0+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppReviewDetail
```

**Response**:

```json
{
    "data": {
        "type": "betaAppReviewDetails",
        "id": "6446998023",
        "attributes": {
            "contactFirstName": "Johnny",
            "contactLastName": "Appleseed",
            "contactPhone": "8001234567",
            "contactEmail": "example@apple.com",
            "demoAccountName": null,
            "demoAccountPassword": null,
            "demoAccountRequired": false,
            "notes": null
        },
        "relationships": {
            "app": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/6446998023/relationships/app",
                    "related": "https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/6446998023/app"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/6446998023"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppReviewDetail"
    }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaAppReviewDetail`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[betaAppReviewDetails]` ([string]): Additional fields to include for each beta app review detail resource returned by the response.

  **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `app`

## Responses

- `200` OK (`BetaAppReviewDetailWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting an app’s TestFlight details
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the beta license agreement of an app](./get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [Get the beta license agreement ID for an app](./get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List all beta app localizations of an app](./get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [List beta app localization IDs for an app](./get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betaappreviewdetail)*