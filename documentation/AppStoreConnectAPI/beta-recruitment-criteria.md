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
- [Create Recruitment Criteria](post-v1-betarecruitmentcriteria.md)
  Create new criteria for recruiting testers for your TestFlight build.
- [Modify Recruitment Criteria](patch-v1-betarecruitmentcriteria-_id_.md)
  Update the recruitment criteria for your TestFlight build.
- [Remove recruitment criteria](delete-v1-betarecruitmentcriteria-_id_.md)
  Remove the recruitment criteria for your TestFlight build.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [Read build compatibility for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibility information for a specific beta group.
- [Read recruitment criteria options](get-v1-betarecruitmentcriterionoptions.md)
  Get a list of the possible beta recruitment criteria options.
### Objects
- [object BetaRecruitmentCriterionCompatibleBuildCheck](betarecruitmentcriterioncompatiblebuildcheck.md)
  The result of checking whether a specific build meets the device family and OS version requirements of a beta recruitment criterion.
- [object BetaRecruitmentCriterionCompatibleBuildCheckResponse](betarecruitmentcriterioncompatiblebuildcheckresponse.md)
  A response containing a single result of checking whether a build meets the requirements of a beta recruitment criterion.
- [object BetaRecruitmentCriterion](betarecruitmentcriterion.md)
  A rule that controls which testers are automatically invited to a beta group based on device family and OS version.
- [object BetaRecruitmentCriterionCreateRequest](betarecruitmentcriterioncreaterequest.md)
  The request body you use to create a beta recruitment criterion.
- [object BetaRecruitmentCriterionOption](betarecruitmentcriterionoption.md)
  A specific device family and OS version combination available as a value for a beta recruitment criterion.
- [object BetaRecruitmentCriterionResponse](betarecruitmentcriterionresponse.md)
  A response containing a single beta recruitment criterion and its configured device/OS requirements.
- [object BetaRecruitmentCriterionUpdateRequest](betarecruitmentcriterionupdaterequest.md)
  The request body for updating the device family and OS version requirements of a beta recruitment criterion.
- [object BetaPublicLinkUsagesV1MetricResponse](betapubliclinkusagesv1metricresponse.md)
  A metrics response containing usage data for a TestFlight public invite link, showing tester enrollment trends.
- [type DeviceFamily](devicefamily.md)
  String that represents a device family.
- [object DeviceFamilyOsVersionFilter](devicefamilyosversionfilter.md)
  The object that you use to specify a device family and operating system to use for your beta recruitment criteria.
- [object BetaRecruitmentCriterionOptionsResponse](betarecruitmentcriterionoptionsresponse.md)
  A response containing a list of device family and OS version options for configuring a beta recruitment criterion.

## See Also

- [Beta Testers](beta-testers.md)
  People who can install and test prerelease builds.
- [Beta Tester Invitations](beta-tester-invitations.md)
  Requests to send or resend an email inviting a beta tester to test an app.
- [Beta Groups](beta-groups.md)
  Groups of beta testers that have access to one or more builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-recruitment-criteria)*