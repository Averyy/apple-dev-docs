# InApps.Relationships.InAppsAppRelationship.Apps.Attributes

**Framework**: Device Management  
**Kind**: dictionary

## Declaration

```swift
object InApps.Relationships.InAppsAppRelationship.Apps.Attributes
```

## Topics

### Dictionaries
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.Artwork](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/artwork-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.ContentRatingsBySystem](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/contentratingsbysystem-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.DescriptionAttribute](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/descriptionattribute.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.FileSizeByDevice](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/filesizebydevice-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.LatestVersionInfo](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/latestversioninfo-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.Offers](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/offers-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.RequirementsByDeviceFamily](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/requirementsbydevicefamily-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.ScreenshotsByType](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/screenshotsbytype-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.TaxExclusivePrices](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/taxexclusiveprices-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.UserRating](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/userrating-data.dictionary.md)
- [object InApps.Relationships.InAppsAppRelationship.Apps.Attributes.VersionHistory](inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary/versionhistory-data.dictionary.md)

## Properties

- `artistName` (string) *(required)*
- `artwork` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.Artwork) *(required)*
- `bundleId` (string) *(required)*
- `contentRatingsBySystem` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.ContentRatingsBySystem) *(required)*
- `description` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.DescriptionAttribute)
- `deviceFamilies` ([string]) *(required)*
- `externalVersionId` (int32) *(required)*
- `fileSizeByDevice` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.FileSizeByDevice)
- `genreDisplayName` (string)
- `hasEula` (boolean) *(required)*
- `isB2BCustomApp` (boolean) *(required)*
- `isFirstPartyHideableApp` (boolean) *(required)*
- `isIOSBinaryMacOSCompatible` (boolean) *(required)*
- `isVisionOSCompatible` (boolean)
- `isVppDeviceBasedLicensingEnabled` (boolean) *(required)*
- `languageList` ([string])
- `latestVersionInfo` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.LatestVersionInfo)
- `macRequiredCapabilities` (string)
- `minimumMacOSVersion` (string)
- `minimumOSVersion` (string) *(required)*
- `minimumVisionOSVersion` (string)
- `name` (string) *(required)*
- `offers` ([InApps.Relationships.InAppsAppRelationship.Apps.Attributes.Offers]) *(required)*
- `privacyPolicyUrl` (string)
- `requiredCapabilities` (string)
- `requiredCapabilitiesForRealityDevice` (string)
- `requirementsByDeviceFamily` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.RequirementsByDeviceFamily)
- `screenshotsByType` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.ScreenshotsByType)
- `seller` (string)
- `subtitle` (string)
- `supportURLForLanguage` (string)
- `supportsDeviceSharing` (boolean)
- `taxExclusivePrices` ([InApps.Relationships.InAppsAppRelationship.Apps.Attributes.TaxExclusivePrices])
- `taxRate` (number)
- `url` (string) *(required)*
- `userRating` (InApps.Relationships.InAppsAppRelationship.Apps.Attributes.UserRating) *(required)*
- `usesClassKit` (boolean)
- `versionHistory` ([InApps.Relationships.InAppsAppRelationship.Apps.Attributes.VersionHistory])
- `watchBundleId` (string)
- `websiteUrl` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/inapps/relationships-data.dictionary/inappsapprelationship/apps/attributes-data.dictionary)*