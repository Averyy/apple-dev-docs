# BetaFeedbackScreenshotSubmission.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a `BetaFeedbackScreenshotSubmission` resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object BetaFeedbackScreenshotSubmission.Attributes
```

## Properties

- `appPlatform` (Platform)
- `appUptimeInMilliseconds` (int64): **Minimum**: `0`; **Maximum**: `9007199254740991`
- `architecture` (string)
- `batteryPercentage` (integer)
- `buildBundleId` (string)
- `comment` (string)
- `connectionType` (DeviceConnectionType)
- `createdDate` (date-time)
- `deviceFamily` (DeviceFamily)
- `deviceModel` (string)
- `devicePlatform` (Platform)
- `diskBytesAvailable` (int64): **Minimum**: `0`; **Maximum**: `9007199254740991`
- `diskBytesTotal` (int64): **Minimum**: `0`; **Maximum**: `9007199254740991`
- `email` (string)
- `locale` (string)
- `osVersion` (string)
- `pairedAppleWatch` (string)
- `screenHeightInPoints` (integer)
- `screenWidthInPoints` (integer)
- `screenshots` ([BetaFeedbackScreenshotImage])
- `timeZone` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betafeedbackscreenshotsubmission/attributes-data.dictionary)*