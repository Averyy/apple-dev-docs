# Read the Beta License Agreement of an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the beta license agreement for a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaLicenseAgreement
```

**Response**:

```json
{
    "data": {
        "type": "betaLicenseAgreements",
        "id": "66237ae8-4920-497d-90f5-3f9acc76ec95",
        "attributes": {
            "agreementText": "This is the Beta License Agreement for your Your Next Cortado. You are testing pre-release version of this app. Here are some more thoughts about a beta coffee app. The coffee might not be dialed in and you may experience less than perfect coffee."
        },
        "relationships": {
            "app": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements/66237ae8-4920-497d-90f5-3f9acc76ec95/relationships/app",
                    "related": "https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements/66237ae8-4920-497d-90f5-3f9acc76ec95/app"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements/66237ae8-4920-497d-90f5-3f9acc76ec95"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaLicenseAgreement"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaLicenseAgreement`

## Parameters

- `fields[betaLicenseAgreements]` ([string]): Fields to return for included related types.

## See Also

- [Read the Beta App Review Details Resource of an App](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [GET /v1/apps/{id}/relationships/betaAppReviewDetail](get-v1-apps-_id_-relationships-betaappreviewdetail.md)
- [GET /v1/apps/{id}/relationships/betaLicenseAgreement](get-v1-apps-_id_-relationships-betalicenseagreement.md)
- [List All Beta App Localizations of an App](get-v1-apps-_id_-betaapplocalizations.md)
  Get a list of localized beta test information for a specific app.
- [GET /v1/apps/{id}/relationships/betaAppLocalizations](get-v1-apps-_id_-relationships-betaapplocalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betalicenseagreement)*