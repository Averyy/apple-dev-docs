# Read build compatibility for a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the build compatibility information for a specific beta group.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/betaRecruitmentCriterionCompatibleBuildCheck`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the beta group resource ID from the [`List beta groups`](./get-v1-betagroups.md) response.

### Query Parameters

- `fields[betaRecruitmentCriterionCompatibleBuildChecks]` ([string]): **Allowed Values**: `hasCompatibleBuild`

## Responses

- `200` OK (`BetaRecruitmentCriterionCompatibleBuildCheckResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Beta Group Information
- [List beta groups](./get-v1-betagroups.md)
  Find and list beta groups for all apps.
- [Read beta group information](./get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the app information of a beta group](./get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [Get the app ID for a beta group](./get-v1-betagroups-_id_-relationships-app.md)
- [Read Metrics for Beta Testers in a Beta Group](./get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read Recruitment Criteria for a Beta Group](./get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [List beta recruitment criterion IDs for a beta group](./get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Get the compatible build check ID for a beta group recruitment criterion](./get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck)*