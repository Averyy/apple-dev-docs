# Read the Beta App Review Details Resource of an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the beta app review details for a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[betaAppReviewDetails]` ([string]): Fields to return for included related types.

## See Also

- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the Beta License Agreement of an App](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [GET /v1/apps/{id}/relationships/betaLicenseAgreement](get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List All Beta App Localizations of an App](get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppLocalizations](get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betaappreviewdetail)*