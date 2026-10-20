# List all beta app localizations of an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of localized beta test information for a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppLocalizations
```

**Response**:

```json
{
    "data": [
        {
            "type": "betaAppLocalizations",
            "id": "318d7ad7-6d08-403d-84f4-1eb8d9ba9071",
            "attributes": {
                "feedbackEmail": "example@apple.com",
                "marketingUrl": null,
                "privacyPolicyUrl": null,
                "tvOsPrivacyPolicy": null,
                "description": null,
                "locale": "en-US"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/318d7ad7-6d08-403d-84f4-1eb8d9ba9071/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/318d7ad7-6d08-403d-84f4-1eb8d9ba9071/app"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/318d7ad7-6d08-403d-84f4-1eb8d9ba9071"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppLocalizations"
    },
    "meta": {
        "paging": {
            "total": 1,
            "limit": 50
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaAppLocalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[betaAppLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `feedbackEmail`, `marketingUrl`, `privacyPolicyUrl`, `tvOsPrivacyPolicy`, `description`, `locale`, `app`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`BetaAppLocalizationsWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting an app’s TestFlight details
- [Read the beta app review details resource of an app](./get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Get the beta app review detail ID for an app](./get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the beta license agreement of an app](./get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [Get the beta license agreement ID for an app](./get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List beta app localization IDs for an app](./get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betaapplocalizations)*