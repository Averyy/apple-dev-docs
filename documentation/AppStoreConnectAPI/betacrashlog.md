# BetaCrashLog

**Framework**: App Store Connect API  
**Kind**: dictionary

The crash log details from a TestFlight tester’s device, including the stack trace and metadata captured at the time of the crash.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object BetaCrashLog
```

## Topics

### Dictionaries
- [object BetaCrashLog.Attributes](betacrashlog/attributes-data.dictionary.md)
  Attributes that describe a beta crash log resource.

## Properties

- `attributes` (BetaCrashLog.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object BetaCrashLogResponse](betacrashlogresponse.md)
  A response containing a single crash log from a TestFlight tester’s device.
- [object BetaFeedbackCrashSubmission](betafeedbackcrashsubmission.md)
  A crash report submitted by a TestFlight beta tester, linked to the build, bundle, and tester that produced it.
- [object BetaFeedbackCrashSubmissionResponse](betafeedbackcrashsubmissionresponse.md)
  A response containing a single crash report submitted by a TestFlight beta tester.
- [object BetaFeedbackCrashSubmissionsResponse](betafeedbackcrashsubmissionsresponse.md)
  A response containing a list of crash reports submitted by TestFlight beta testers.
- [object BetaFeedbackCrashSubmissionCrashLogLinkageResponse](betafeedbackcrashsubmissioncrashloglinkageresponse.md)
  A response containing the resource identifier of the crash log linked to a crash feedback submission.
- [type DeviceConnectionType](deviceconnectiontype.md)
  A string that represents the ways a device was connected for a specific crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betacrashlog)*