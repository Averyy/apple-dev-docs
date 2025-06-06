# Beta recruitment criteria

**Framework**: App Store Connect API

Create public links that accept testers with specific device and OS combinations.

#### Overview

Use the `betaRecruitmentCriteria` resource to create public links with Device and OS criteria that help improve beta recruitment. Gain insights on the public-link performance from tester-event metrics, so you can modify the criteria set for the public, and enable or disable a public link.

Team keys or individual keys with these roles can use this this resource:

- Account holder
- Admin
- App Managers

## Topics

### Resending Invitations
- [Create recruitment criteria](post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Modify recruitment criteria](patch-v1-betarecruitmentcriteria-_id_.md)
  Update the recruitment criteria for your TestFlight build.
- [Remove recruitment criteria ](delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read recruitment criteria for a beta group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read build compatibilty for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibilty information for a specific beta group.
- [Read recruitment criteria options](get-v1-betarecruitmentcriterionoptions.md)
  Get a list of the possible beta recruitment criteria options.
### Objects
- [object BetaRecruitmentCriterionCompatibleBuildCheck](betarecruitmentcriterioncompatiblebuildcheck.md)
  The data structure that represents a beta recruitment criteria-compatible, build-check resource.
- [object BetaRecruitmentCriterionCompatibleBuildCheckResponse](betarecruitmentcriterioncompatiblebuildcheckresponse.md)
  A response that contains a single beta recruitment criteria-compatible, build-check resource.
- [object BetaRecruitmentCriterion](betarecruitmentcriterion.md)
  The data structure that represents a beta recruitment criterion resource.
- [object BetaRecruitmentCriterionCreateRequest](betarecruitmentcriterioncreaterequest.md)
  The request body you use to create a beta recruitment criterion.
- [object BetaRecruitmentCriterionOption](betarecruitmentcriterionoption.md)
- [object BetaRecruitmentCriterionResponse](betarecruitmentcriterionresponse.md)
  A response that contains a single beta recruitment criterion resource.
- [object BetaRecruitmentCriterionUpdateRequest](betarecruitmentcriterionupdaterequest.md)
  The request body you use to update a beta recruitment criterion resource.
- [object BetaPublicLinkUsagesV1MetricResponse](betapubliclinkusagesv1metricresponse.md)
- [type DeviceFamily](devicefamily.md)
  String that represents a device family.
- [object DeviceFamilyOsVersionFilter](devicefamilyosversionfilter.md)
  The object that you use to specify a device family and operating system to use for your beta recruitment criteria.
- [object BetaRecruitmentCriterionOptionsResponse](betarecruitmentcriterionoptionsresponse.md)

## See Also

- [Beta Testers](beta-testers.md)
  People who can install and test prerelease builds.
- [Beta Tester Invitations](beta-tester-invitations.md)
  Requests to send or resend an email inviting a beta tester to test an app.
- [Beta Groups](beta-groups.md)
  Groups of beta testers that have access to one or more builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-recruitment-criteria)*