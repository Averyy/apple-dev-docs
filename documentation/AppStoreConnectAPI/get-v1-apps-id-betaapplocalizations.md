# List All Beta App Localizations of an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized beta test information for a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[betaAppLocalizations]` ([string]): Fields to return for included related types.
- `limit` (integer): Number of resources to return.

## See Also

- [Read the Beta App Review Details Resource of an App](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [Read the Beta License Agreement of an App](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [GET /v1/apps/{id}/relationships/betaLicenseAgreement](get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [GET /v1/apps/{id}/relationships/betaAppLocalizations](get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betaapplocalizations)*