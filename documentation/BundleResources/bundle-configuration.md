# Bundle configuration

**Framework**: Bundle Resources

Define basic characteristics of a bundle, like its name, type, and version.

#### Overview

The [`Information Property List`](information-property-list.md) file associated with a bundle tells you how to interpret the bundle’s contents. The file describes fundamental features, like whether the bundle contains an app, a framework, or something else. It also includes identifying characteristics of the bundle, like an identifier, a human-readable name, and a version.

## Topics

### Categorization
- [CFBundlePackageType](information-property-list/cfbundlepackagetype.md)
  The type of bundle.
- [LSApplicationCategoryType](information-property-list/lsapplicationcategorytype.md)
  The category that best describes your app for the App Store.
### Identification
- [CFBundleIdentifier](information-property-list/cfbundleidentifier.md)
  A unique identifier for a bundle.
- [WKAppBundleIdentifier](information-property-list/wkappbundleidentifier.md)
  The bundle ID of the watchOS app.
- [WKCompanionAppBundleIdentifier](information-property-list/wkcompanionappbundleidentifier.md)
  The bundle ID of the watchOS app’s companion iOS app.
### Naming
- [CFBundleName](information-property-list/cfbundlename.md)
  A user-visible short name for the bundle.
- [CFBundleDisplayName](information-property-list/cfbundledisplayname.md)
  The user-visible name for the bundle, used by Siri and visible on the iOS Home screen.
- [CFBundleSpokenName](information-property-list/cfbundlespokenname.md)
  A replacement for the app name in text-to-speech operations.
### Bundle version
- [CFBundleVersion](information-property-list/cfbundleversion.md)
  The version of the build that identifies an iteration of the bundle.
- [CFBundleShortVersionString](information-property-list/cfbundleshortversionstring.md)
  The release or version number of the bundle.
- [CFBundleInfoDictionaryVersion](information-property-list/cfbundleinfodictionaryversion.md)
  The current version of the Information Property List structure.
- [NSHumanReadableCopyright](information-property-list/nshumanreadablecopyright.md)
  A human-readable copyright notice for the bundle.
### Operating system version
- [LSMinimumSystemVersion](information-property-list/lsminimumsystemversion.md)
  The minimum version of the operating system required for the app to run in macOS.
- [LSMinimumSystemVersionByArchitecture](information-property-list/lsminimumsystemversionbyarchitecture.md)
  The minimum version of macOS required for the app to run on a set of architectures.
- [MinimumOSVersion](information-property-list/minimumosversion.md)
  The minimum version of the operating system required for the app to run in iOS, iPadOS, tvOS, and watchOS.
- [LSRequiresIPhoneOS](information-property-list/lsrequiresiphoneos.md)
  A Boolean value indicating whether the app must run in iOS.
- [WKApplication](information-property-list/wkapplication.md)
- [WKWatchKitApp](information-property-list/wkwatchkitapp.md)
  A Boolean value that indicates whether the bundle is a watchOS app.
### Localization
- [CFBundleDevelopmentRegion](information-property-list/cfbundledevelopmentregion.md)
  The default language and region for the bundle, as a language ID.
- [CFBundleLocalizations](information-property-list/cfbundlelocalizations.md)
  The localizations handled manually by your app.
- [CFBundleAllowMixedLocalizations](information-property-list/cfbundleallowmixedlocalizations.md)
  A Boolean value that indicates whether the bundle supports the retrieval of localized strings from frameworks.
- [TICapsLockLanguageSwitchCapable](information-property-list/ticapslocklanguageswitchcapable.md)
  A Boolean value that enables the Caps Lock key to switch between Latin and non-Latin input sources.
### Help
- [CFAppleHelpAnchor](information-property-list/cfapplehelpanchor.md)
  The name of the bundle’s HTML help file.
- [CFBundleHelpBookName](information-property-list/cfbundlehelpbookname.md)
  The name of the help file that will be opened in Help Viewer.
- [CFBundleHelpBookFolder](information-property-list/cfbundlehelpbookfolder.md)
  The name of the folder containing the bundle’s help files.

## See Also

- [User interface](user-interface.md)
  Configure an app’s scenes, storyboards, icons, fonts, and other user interface elements.
- [App execution](app-execution.md)
  Control app launch, execution, and termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/bundle-configuration)*