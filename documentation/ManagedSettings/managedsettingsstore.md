# ManagedSettingsStore

**Framework**: ManagedSettings  
**Kind**: class

A data store that applies settings to the current user or device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class ManagedSettingsStore
```

## Mentions

- [Confirming the Effective TV and Movie Ratings](readingmedia.md)

#### Overview

The Managed Settings data store groups settings according to function. Each group contains relevant data about its associated settings, for example, a default value and minimum and maximum possible values.

##### Configure Settings

Use the settings objects to inspect your application’s current configurations as well as apply new configurations. Changing the value of a setting to `nil` deletes your app’s configuration for that setting from the device. The system doesn’t guarantee that the settings you specify govern the device’s behavior. The system is responsible for determining its effective state based on all the settings it receives.

##### Examine Effective Settings

In a few cases, you can also access the effective settings. For example, a media app can access the effective rating settings to filter the content it offers, even though it doesn’t provide configurations for these or any other settings. Subscribe to [`$effectiveMaximumTVShowRating`](managedsettingsstore/$effectivemaximumtvshowrating.md) or [`$effectiveMaximumMovieRating`](managedsettingsstore/$effectivemaximummovierating.md) to determine what TV shows or movies to offer.

## Topics

### Creating the Store
- [init()](managedsettingsstore/init.md)
  Creates a new instance of a store.
### Managing a Settings Group
- [protocol ManagedSettingsGroup](managedsettingsgroup.md)
  A group of settings to manage.
### Restricting Device Settings
- [var account: AccountSettings](managedsettingsstore/account.md)
  Settings that affect accounts.
- [struct AccountSettings](accountsettings.md)
  An object that configures whether a user can modify their device’s account settings.
- [var cellular: CellularSettings](managedsettingsstore/cellular.md)
  Settings that affect cellular networking.
- [struct CellularSettings](cellularsettings.md)
  Constraints on the user’s cellular networking settings.
- [var dateAndTime: DateAndTimeSettings](managedsettingsstore/dateandtime.md)
  Settings that affect the date and time.
- [struct DateAndTimeSettings](dateandtimesettings.md)
  Constraints on the device’s date and time settings.
- [var passcode: PasscodeSettings](managedsettingsstore/passcode.md)
  Settings that affect the device passcode.
- [struct PasscodeSettings](passcodesettings.md)
  Constraints on a user’s ability to change their device’s passcode.
- [var shield: ShieldSettings](managedsettingsstore/shield.md)
  Settings that affect what activities the system covers with a shielding view on this device.
- [struct ShieldSettings](shieldsettings.md)
  Constraints that indicate what apps and websites to cover with a shielding view.
- [var siri: SiriSettings](managedsettingsstore/siri.md)
  Settings that affect Siri.
- [struct SiriSettings](sirisettings.md)
  Constraints on the device’s Siri settings.
### Filtering Media Content
- [var appStore: AppStoreSettings](managedsettingsstore/appstore.md)
  Settings that affect the App Store.
- [struct AppStoreSettings](appstoresettings.md)
  Constraints on a user’s App Store settings.
- [var application: ApplicationSettings](managedsettingsstore/application.md)
  Settings that affect applications.
- [struct ApplicationSettings](applicationsettings.md)
  Constraints on the apps and categories of apps a user can run on their device.
- [var effectiveMaximumMovieRating: Int](managedsettingsstore/effectivemaximummovierating.md)
  The movie rating constraint that is active on this device.
- [var effectiveMaximumTVShowRating: Int](managedsettingsstore/effectivemaximumtvshowrating.md)
  The TV rating constraint that is active on this device.
- [var gameCenter: GameCenterSettings](managedsettingsstore/gamecenter.md)
  Settings that affect Game Center.
- [struct GameCenterSettings](gamecentersettings.md)
  Constraints on the user’s Game Center settings.
- [var media: MediaSettings](managedsettingsstore/media.md)
  Settings that affect media.
- [struct MediaSettings](mediasettings.md)
  Constraints on the media content the user can access.
### Restricting Web Content
- [var safari: SafariSettings](managedsettingsstore/safari.md)
  Settings that affect Safari’s search results and cookie policies.
- [struct SafariSettings](safarisettings.md)
  Constraints on Safari’s AutoFill and cookie behaviors.
- [var webContent: WebContentSettings](managedsettingsstore/webcontent.md)
  Settings that affect web content.
- [struct WebContentSettings](webcontentsettings.md)
  An object that configures which websites a user can access.
### Accessing Metadata
- [struct BoundedSettingMetadata](boundedsettingmetadata.md)
  Additional information about a bounded setting.
- [struct SettingMetadata](settingmetadata.md)
  Additional information about a configurable setting.
### Observing Current Settings
- [var objectWillChange: ObservableObjectPublisher](managedsettingsstore/objectwillchange.md)
- [var $effectiveMaximumMovieRating: Published<Int>.Publisher](managedsettingsstore/$effectivemaximummovierating.md)
  The movie rating constraint that is active on this device.
- [var $effectiveMaximumTVShowRating: Published<Int>.Publisher](managedsettingsstore/$effectivemaximumtvshowrating.md)
  The television show rating constraint that is active on this device.
- [ManagedSettingsStore.ObjectWillChangePublisher](managedsettingsstore/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.
### Structures
- [ManagedSettingsStore.Name](managedsettingsstore/name.md)
  The unique name of a store.
### Initializers
- [convenience init(named: ManagedSettingsStore.Name)](managedsettingsstore/init(named:).md)
  Creates a new instance of a store with a custom name.
### Instance Methods
- [func clearAllSettings()](managedsettingsstore/clearallsettings.md)
  Clears all settings for this store.
### Default Implementations
- [ObservableObject Implementations](managedsettingsstore/observableobject-implementations.md)

## Relationships

### Conforms To
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore)*