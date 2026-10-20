# Read recruitment criteria options

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of the possible beta recruitment criteria options.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaRecruitmentCriterionOptions`

## Parameters

### Query Parameters

- `fields[betaRecruitmentCriterionOptions]` ([string]): **Allowed Values**: `deviceFamilyOsVersions`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`BetaRecruitmentCriterionOptionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Resending Invitations
- [Create Recruitment Criteria](./post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Modify Recruitment Criteria](./patch-v1-betarecruitmentcriteria-_id_.md)
  Update the recruitment criteria for your TestFlight build.
- [Remove recruitment criteria](./delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read Recruitment Criteria for a Beta Group](./get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read build compatibility for a beta group](./get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibility information for a specific beta group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betarecruitmentcriterionoptions)*