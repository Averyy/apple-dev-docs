# AssetInventory

**Framework**: Speech  
**Kind**: class

Before using `SpeechAnalyzer`, you must install the assets required by the modules you use. These assets are machine-learning models downloaded from Apple’s servers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class AssetInventory
```

#### Overview

Once you have created the modules you wish to use, installation is a three-step process:

- Allocate the locales used by the modules. You may only allocate a limited number of locales at one time. This is done to limit the storage space and network usage. This is not required for modules whose assets are the same for all locales.
- Start the download of the required assets. You don’t have to download again when you create new modules; the assets only depend on the configuration of each module, but not the module’s object identity.
- Wait for the downloads to finish. Note that downloading may have already happened, because: - The assets were preinstalled on the system.
- Another app already downloaded the assets.
- A different configuration of modules you previously used happen to use the same assets.

All of these actions persist across launches of your app. Assets are shared between apps, so duplicates aren’t downloaded multiple times, and don’t take up storage space. However, the system may unsubscribe your app from assets that haven’t been used in a while.

Note that your app is never told about what assets are required, it only deals with the module objects and how they are configured.

## Topics

### Type Properties
- [static var allocatedLocales: [Locale]](assetinventory/allocatedlocales.md)
  Before you can subscribe to assets supporting a module, you must allocate the locale used by that module.
- [static var maximumAllocatedLocales: Int](assetinventory/maximumallocatedlocales.md)
  The number of locale allocations permitted to an application.
### Type Methods
- [static func allocate(locale: Locale) async throws -> Bool](assetinventory/allocate(locale:).md)
  Adds the locale to `allocatedLocales`. Throws if the number of locales would exceed `maximumAllocatedLocales`. Returns false if the locale is already in the set.
- [static func assetInstallationRequest(supporting: [any SpeechModule]) async throws -> AssetInstallationRequest?](assetinventory/assetinstallationrequest(supporting:).md)
  Returns an `AssetsInstallationRequest` object, which is used to initiate the asset download and monitor the progress.
- [static func deallocate(locale: Locale) async -> Bool](assetinventory/deallocate(locale:).md)
  Removes the locale from `allocatedLocales`. Returns false if the locale is not in the set.
- [static func status(forModules: [any SpeechModule]) async -> AssetInventory.Status](assetinventory/status(formodules:).md)
  Returns the status for the list of modules. If the status differs between modules, it returns the lowest status.
### Enumerations
- [AssetInventory.Status](assetinventory/status.md)

## See Also

- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [actor SpeechAnalyzer](speechanalyzer.md)
  Analyzes spoken audio content in various ways and manages the analysis session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory)*