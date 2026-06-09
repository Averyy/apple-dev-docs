# Read build compatibility for a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the build compatibility information for a specific beta group.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/betaRecruitmentCriterionCompatibleBuildCheck`

## Parameters

- `fields[betaRecruitmentCriterionCompatibleBuildChecks]` ([string])

## See Also

- [List beta groups](get-v1-betagroups.md)
  Find and list beta groups for all apps.
- [Read beta group information](get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the app information of a beta group](get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [Get the app ID for a beta group](get-v1-betagroups-_id_-relationships-app.md)
- [Read Metrics for Beta Testers in a Beta Group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [List beta recruitment criterion IDs for a beta group](get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Get the compatible build check ID for a beta group recruitment criterion](get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck)*