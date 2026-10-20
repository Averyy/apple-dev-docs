# Modify Recruitment Criteria

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the recruitment criteria for your TestFlight build.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaRecruitmentCriteria/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the beta recruitment criteria resource ID from the [`Read Recruitment Criteria for a Beta Group`](./get-v1-betagroups-_id_-betarecruitmentcriteria.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaRecruitmentCriterionUpdateRequest`

## Responses

- `200` OK (`BetaRecruitmentCriterionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Resending Invitations
- [Create Recruitment Criteria](./post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Remove recruitment criteria](./delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read Recruitment Criteria for a Beta Group](./get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read build compatibility for a beta group](./get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibility information for a specific beta group.
- [Read recruitment criteria options](./get-v1-betarecruitmentcriterionoptions.md)
  Get a list of the possible beta recruitment criteria options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betarecruitmentcriteria-_id_)*