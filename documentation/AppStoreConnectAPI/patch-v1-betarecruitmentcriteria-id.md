# Modify Recruitment Criteria

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the recruitment criteria for your TestFlight build.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaRecruitmentCriteria/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the beta recruitment criteria resource ID from the [`Read Recruitment Criteria for a Beta Group`](get-v1-betagroups-_id_-betarecruitmentcriteria.md) response.

## See Also

- [Create Recruitment Criteria](post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Remove Recruitment Criteria](delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read Build Compatibilty for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibilty information for a specific beta group.
- [Read Recruitment Criteria Options](get-v1-betarecruitmentcriterionoptions.md)
  Get a list of the possible beta recruitment criteria options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betarecruitmentcriteria-_id_)*