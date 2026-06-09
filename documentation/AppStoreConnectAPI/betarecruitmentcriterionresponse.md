# BetaRecruitmentCriterionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single beta recruitment criterion and its configured device/OS requirements.

**Availability**:
- App Store Connect API 3.8+

## Declaration

```swift
object BetaRecruitmentCriterionResponse
```

## Properties

- `data` (BetaRecruitmentCriterion) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betarecruitmentcriterionresponse)*