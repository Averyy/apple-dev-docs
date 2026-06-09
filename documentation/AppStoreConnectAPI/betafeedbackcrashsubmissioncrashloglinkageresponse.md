# BetaFeedbackCrashSubmissionCrashLogLinkageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifier of the crash log linked to a crash feedback submission.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object BetaFeedbackCrashSubmissionCrashLogLinkageResponse
```

## Topics

### Dictionaries
- [object BetaFeedbackCrashSubmissionCrashLogLinkageResponse.Data](betafeedbackcrashsubmissioncrashloglinkageresponse/data-data.dictionary.md)

## Properties

- `data` (BetaFeedbackCrashSubmissionCrashLogLinkageResponse.Data) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object BetaCrashLog](betacrashlog.md)
  The crash log details from a TestFlight tester’s device, including the stack trace and metadata captured at the time of the crash.
- [object BetaCrashLogResponse](betacrashlogresponse.md)
  A response containing a single crash log from a TestFlight tester’s device.
- [object BetaFeedbackCrashSubmission](betafeedbackcrashsubmission.md)
  A crash report submitted by a TestFlight beta tester, linked to the build, bundle, and tester that produced it.
- [object BetaFeedbackCrashSubmissionResponse](betafeedbackcrashsubmissionresponse.md)
  A response containing a single crash report submitted by a TestFlight beta tester.
- [object BetaFeedbackCrashSubmissionsResponse](betafeedbackcrashsubmissionsresponse.md)
  A response containing a list of crash reports submitted by TestFlight beta testers.
- [type DeviceConnectionType](deviceconnectiontype.md)
  A string that represents the ways a device was connected for a specific crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betafeedbackcrashsubmissioncrashloglinkageresponse)*