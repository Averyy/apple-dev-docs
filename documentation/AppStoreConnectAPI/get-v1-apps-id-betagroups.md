# List All Beta Groups for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of beta groups associated with a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaGroups
```

**Response**:

```json
{
    “data”: [
        {
            “type”: “betaGroups”,
            “id”: “26b3c3c4-aeb1-4d24-be6a-80c554f671a2”,
            “attributes”: {
                “name”: “Internal Test Group”,
                “createdDate”: “2022-09-07T18:25:13.582Z”,
                “isInternalGroup”: true,
                “hasAccessToAllBuilds”: true,
                “publicLinkEnabled”: null,
                “publicLinkId”: null,
                “publicLinkLimitEnabled”: null,
                “publicLinkLimit”: null,
                “publicLink”: null,
                “feedbackEnabled”: true,
                “iosBuildsAvailableForAppleSiliconMac”: true
            },

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaGroups`

## Parameters

- `fields[betaGroups]` ([string]): Fields to return for included related types.
- `limit` (integer): Number of resources to return.

## See Also

- [GET /v1/apps/{id}/relationships/betaGroups](get-v1-apps-_id_-relationships-betagroups.md)
- [Remove Specified Beta Testers From All Groups and Builds of an App](delete-v1-apps-_id_-relationships-betatesters.md)
  Remove one or more beta testers’ access to test any builds of a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betagroups)*