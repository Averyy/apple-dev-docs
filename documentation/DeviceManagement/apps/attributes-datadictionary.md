# Apps.Attributes

**Framework**: Device Management  
**Kind**: dictionary

The attributes for an apps resource.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Apps.Attributes
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

## Topics

### Related Objects
- [object Apps.Attributes.ContentRatingsBySystem](apps/attributes-data.dictionary/contentratingsbysystem-data.dictionary.md)
- [object Apps.Attributes.FileSizeByDevice](apps/attributes-data.dictionary/filesizebydevice-data.dictionary.md)
- [object Apps.Attributes.LatestVersionInfo](apps/attributes-data.dictionary/latestversioninfo-data.dictionary.md)
- [object Apps.Attributes.Offers](apps/attributes-data.dictionary/offers-data.dictionary.md)
- [object Apps.Attributes.RequirementsByDeviceFamily](apps/attributes-data.dictionary/requirementsbydevicefamily-data.dictionary.md)
- [object Apps.Attributes.ScreenshotsByType](apps/attributes-data.dictionary/screenshotsbytype-data.dictionary.md)
- [object Apps.Attributes.TaxExclusivePrices](apps/attributes-data.dictionary/taxexclusiveprices-data.dictionary.md)
- [object Apps.Attributes.UserRating](apps/attributes-data.dictionary/userrating-data.dictionary.md)
- [object Apps.Attributes.VersionHistory](apps/attributes-data.dictionary/versionhistory-data.dictionary.md)

## Properties

- `artistName` (string) *(required)*: The name of the artist for this content.
- `artwork` (Artwork) *(required)*: The artwork for this content.
- `bundleId` (string) *(required)*: The bundle identifier string associated with this content.
- `contentRatingsBySystem` (Apps.Attributes.ContentRatingsBySystem) *(required)*: Rating and advisory information (may be multiple per item).
- `description` (DescriptionAttribute): The description for the content.
- `deviceFamilies` ([string]) *(required)*: The device families the app supports.
- `externalVersionId` (integer) *(required)*: The external version identifier.
- `fileSizeByDevice` (Apps.Attributes.FileSizeByDevice): **(Extended)** A list of app file sizes by device.
- `genreDisplayName` (string): The localized genre name for display purposes.
- `hasEula` (boolean) *(required)*: A Boolean indicating whether the resource has a EULA.
- `isB2BCustomApp` (boolean) *(required)*: A Boolean indicating whether the app is a B2B Custom App.
- `isFirstPartyHideableApp` (boolean) *(required)*: A Boolean indicating whether the app is a hideable first-party app.
- `isIOSBinaryMacOSCompatible` (boolean) *(required)*
- `isVisionOSCompatible` (boolean)
- `isVppDeviceBasedLicensingEnabled` (boolean) *(required)*: A Boolean indicating whether VPP device-based licensing is enabled.
- `languageList` ([string]): **(Extended)** The language list for the app.
- `latestVersionInfo` (Apps.Attributes.LatestVersionInfo): **(Extended)** A version info map for the latest version of the app.
- `macRequiredCapabilities` (string)
- `minimumMacOSVersion` (string)
- `minimumOSVersion` (string) *(required)*: The minimum OS version required for an app.
- `minimumVisionOSVersion` (string)
- `name` (string) *(required)*: The (potentially) censored name of the content.
- `offers` ([Apps.Attributes.Offers]) *(required)*: A map of offer and asset information for the associated content.
- `privacyPolicyUrl` (string): **(Extended)** A string for the privacy policy for this app.
- `requiredCapabilities` (string): The required capabilities for this app, if any.
- `requiredCapabilitiesForRealityDevice` (string)
- `requirementsByDeviceFamily` (Apps.Attributes.RequirementsByDeviceFamily): **(Extended)** A map of requirements and supported devices by device family.
- `screenshotsByType` (Apps.Attributes.ScreenshotsByType): **(Extended)** A map of artworks representing screenshots for the app by type string.
- `seller` (string): Seller for the app.
- `subtitle` (string): Subtitle of the app.
- `supportsDeviceSharing` (boolean): A Boolean indicating whether multiple users can share this app on the same device.
- `supportURLForLanguage` (string): **(Extended)** Support URL for language for the app.
- `taxExclusivePrices` ([Apps.Attributes.TaxExclusivePrices]): **(Personalized)** Tax-exclusive prices for this salable.
- `taxRate` (number): **(Personalized)** Tax rate for this salable for the current account.
- `url` (string) *(required)*: A canonical URL to the content that may be used for sharing or linking to the content externally.
- `userRating` (Apps.Attributes.UserRating) *(required)*: User rating information for the content. Also shows current version information for apps.
- `usesClassKit` (boolean): A Boolean indicating whether this app uses the ClassKit deployment framework.
- `versionHistory` ([Apps.Attributes.VersionHistory]): **(Extended)** Version history for the app.
- `watchBundleId` (string): The watch bundle identifier string associated with the app.
- `websiteUrl` (string): **(Extended)** Website URL for the app.

## See Also

- [object Apps.Relationships](apps/relationships-data.dictionary.md)
  The relationships for an apps resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apps/attributes-data.dictionary)*