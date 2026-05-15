# Read Recruitment Criteria Options

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of the possible beta recruitment criteria options.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaRecruitmentCriterionOptions`

## Parameters

- `fields[betaRecruitmentCriterionOptions]` ([string])
- `limit` (integer)

## See Also

- [Create Recruitment Criteria](post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Modify Recruitment Criteria](patch-v1-betarecruitmentcriteria-_id_.md)
  Update the recruitment criteria for your TestFlight build.
- [Remove Recruitment Criteria](delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read Build Compatibilty for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibilty information for a specific beta group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betarecruitmentcriterionoptions)*