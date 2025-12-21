# AssetInventory

**Framework**: Speech  
**Kind**: class

Manages the assets that are necessary for transcription or other analyses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class AssetInventory
```

#### Overview

Before using the [`SpeechAnalyzer`](speechanalyzer.md) class, you must install assets required by the modules you plan to use. These assets are machine-learning models downloaded from Apple’s servers and managed by the system. Once you download, install, or use an asset, the system retains and updates it automatically, and shares it with other apps. The system makes a certain number of locale-specific asset reservations available to your app to limit storage space and network usage.

Your app does not work with assets directly. Instead, your app configures module objects. The system uses the modules’ configuration to determine what assets are relevant.

##### Install Assets

Installing an asset is a four-step process:

1. Create analyzer modules in the configurations that you wish to use. These modules can be discarded when no longer needed; the system installs assets using the modules’ configuration, not their object identity.
2. Assign your app’s asset reservations to those locales. The class does this automatically if needed, but you can also call [`reserve(locale:)`](assetinventory/reserve(locale:).md) to do this manually. This step is only necessary for modules with locale-specific assets; that is, modules conforming to [`LocaleDependentSpeechModule`](localedependentspeechmodule.md). You can skip this step for other modules.
3. Start downloading the required assets for the modules’ configuration. Call [`assetInstallationRequest(supporting:)`](assetinventory/assetinstallationrequest(supporting:).md) to obtain an instance of [`AssetInstallationRequest`](assetinstallationrequest.md) and call its [`downloadAndInstall()`](assetinstallationrequest/downloadandinstall().md) method.
4. Wait for the download to finish. Note that the download may finish immediately; the assets may have already been downloaded if the assets were preinstalled on the system, another app already downloaded them, or a previous module configuration used the same assets.

Once assets are downloaded, they persist between app launches and are shared between apps. The system may unsubscribe your app from assets that haven’t been used in a while.

##### Manage Assets

When your app no longer needs assets for a particular locale, call [`release(reservedLocale:)`](assetinventory/release(reservedlocale:).md) to free up that reservation. The system will remove the assets at a later time.

## Topics

### Downloading and installing assets
- [static func assetInstallationRequest(supporting: [any SpeechModule]) async throws -> AssetInstallationRequest?](assetinventory/assetinstallationrequest(supporting:).md)
  Returns an installation request object, which is used to initiate the asset download and monitor its progress.
### Checking asset status
- [static func status(forModules: [any SpeechModule]) async -> AssetInventory.Status](assetinventory/status(formodules:).md)
  Returns the status for the list of modules.
- [AssetInventory.Status](assetinventory/status.md)
### Type Properties
- [static var maximumReservedLocales: Int](assetinventory/maximumreservedlocales.md)
  The number of locale reservations permitted to an app.
- [static var reservedLocales: [Locale]](assetinventory/reservedlocales.md)
  The app’s current asset locale reservations.
### Type Methods
- [static func release(reservedLocale: Locale) async -> Bool](assetinventory/release(reservedlocale:).md)
  Removes an asset locale reservation.
- [static func reserve(locale: Locale) async throws -> Bool](assetinventory/reserve(locale:).md)
  Add an asset locale to the app’s current reservations.

## See Also

- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [actor SpeechAnalyzer](speechanalyzer.md)
  Analyzes spoken audio content in various ways and manages the analysis session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory)*