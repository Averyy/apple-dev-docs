# ManagedApp

**Framework**: ManagedAppDistribution  
**Kind**: struct

A representation of a managed app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
struct ManagedApp
```

## Mentions

- [Fetching and displaying managed apps](fetching-and-displaying-managed-apps.md)

#### Overview

[`ManagedApp`](managedapp.md) represents a managed app that the framework can install. Use an instance of this object to obtain information about the app.

## Topics

### Obtaining general information
- [let name: String](managedapp/name.md)
  The app’s localized name.
- [let subtitle: String?](managedapp/subtitle.md)
  The app’s localized subtitle.
- [let description: String?](managedapp/description.md)
  The app’s localized description.
- [let fileSize: Measurement<UnitInformationStorage>?](managedapp/filesize.md)
  The size of the app in bytes.
- [func iconURL(fitting: CGSize) -> URL?](managedapp/iconurl(fitting:).md)
  A URL for the icon of the app.
- [func screenshotURLs(fitting: CGSize) -> [URL]](managedapp/screenshoturls(fitting:).md)
  An array of the app’s screenshot URLs.
### Obtaining platform and requirement information
- [let platform: Platform](managedapp/platform-swift.property.md)
  The platform of the app.
- [let requirements: String?](managedapp/requirements.md)
  The app’s localized operating system compatibility requirements.
- [ManagedApp.Platform](managedapp/platform-swift.struct.md)
  The supported platform for the app.
### Obtaining supported languages
- [let languages: [Locale.Language]](managedapp/languages.md)
  The app’s supported languages.
- [let metadataLanguage: Locale.Language?](managedapp/metadatalanguage.md)
  The language of the localized properties of this managed app.
### Obtaining seller information
- [let seller: String?](managedapp/seller.md)
  The app’s localized seller.
- [let developerWebsite: URL?](managedapp/developerwebsite.md)
  The app’s developer website URL.
### Obtaining rating information
- [let genres: [String]](managedapp/genres.md)
  The app’s localized genres.
- [let contentRating: String?](managedapp/contentrating.md)
  The app’s content age rating.
### Obtaining privacy and copyright information
- [let privacyPolicy: URL?](managedapp/privacypolicy.md)
  The app’s privacy policy URL.
- [let copyright: String?](managedapp/copyright.md)
  The app’s copyright information.
- [var licenseAgreement: URL?](managedapp/licenseagreement.md)
  The app’s license agreement URL.
### Obtaining version information
- [let version: String?](managedapp/version.md)
  The app’s version information.
- [let releaseNotes: String?](managedapp/releasenotes.md)
  The app’s localized developer release notes.
- [let releaseDate: Date?](managedapp/releasedate.md)
  The app’s release date.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Fetching and displaying managed apps](fetching-and-displaying-managed-apps.md)
  Provide a consistent app presentation when displaying managed apps.
- [class ManagedAppLibrary](managedapplibrary.md)
  A representation of a library of managed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp)*