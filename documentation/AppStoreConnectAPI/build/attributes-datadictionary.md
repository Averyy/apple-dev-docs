# Build.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a Builds resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object Build.Attributes
```

## Mentions

- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)

## Topics

### Types
- [type BuildAudienceType](buildaudiencetype.md)
  A string that represents the App Store Connect audience for a build.

## Properties

- `expired` (boolean): A Boolean value that indicates if the build has expired. An expired build is unavailable for testing.
- `iconAssetToken` (ImageAsset): The icon of the uploaded build.
- `minOsVersion` (string): The minimum operating system version needed to test a build.
- `processingState` (string): The processing state of the build indicating that it is not yet available for testing.
- `version` (string): The version number of the uploaded build.
- `usesNonExemptEncryption` (boolean): A Boolean value that indicates whether the build uses non-exempt encryption.
- `uploadedDate` (date-time): The date and time the build was uploaded to App Store Connect.
- `expirationDate` (date-time): The date and time the build  will auto-expire and no longer be available for testing.
- `buildAudienceType` (BuildAudienceType)
- `computedMinMacOsVersion` (string)
- `lsMinimumSystemVersion` (string)
- `computedMinVisionOsVersion` (string)

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [object Build.Relationships](build/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build/attributes-data.dictionary)*