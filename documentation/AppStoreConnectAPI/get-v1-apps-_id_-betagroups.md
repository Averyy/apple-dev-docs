# List all beta groups for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of beta groups associated with a specific app.

**Availability**:
- App Store Connect API 1.0+

## Discussion

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[betaGroups]` ([string]): Fields to return for included related types.

  **Allowed Values**: `name`, `createdDate`, `isInternalGroup`, `hasAccessToAllBuilds`, `publicLinkEnabled`, `publicLinkId`, `publicLinkLimitEnabled`, `publicLinkLimit`, `publicLink`, `feedbackEnabled`, `iosBuildsAvailableForAppleSiliconMac`, `iosBuildsAvailableForAppleVision`, `app`, `builds`, `betaTesters`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionCompatibleBuildCheck`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`BetaGroupsWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting beta tester information for TestFlight
- [List beta group IDs for an app](./get-v1-apps-_id_-relationships-betagroups.md)
- [Remove specified beta testers from all groups and builds of an app](./delete-v1-apps-_id_-relationships-betatesters.md)
  Remove one or more beta testers’ access to test any builds of a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betagroups)*