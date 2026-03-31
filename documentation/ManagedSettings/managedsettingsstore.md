# ManagedSettingsStore

**Framework**: Managed Settings  
**Kind**: class

A data store that applies settings to the current user or device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 26.0+

## Declaration

```swift
class ManagedSettingsStore
```

## Mentions

- [Confirming the effective TV and movie ratings](readingmedia.md)

#### Overview

The Managed Settings data store groups settings according to function. Each group contains relevant data about its associated settings, for example, a default value and minimum and maximum possible values.

##### Configure Settings

Use the settings objects to inspect your application’s current configurations as well as apply new configurations. Changing the value of a setting to `nil` deletes your app’s configuration for that setting from the device. The system doesn’t guarantee that the settings you specify govern the device’s behavior. The system is responsible for determining its effective state based on all the settings it receives.

##### Examine Effective Settings

In a few cases, you can also access the effective settings. For example, a media app can access the effective rating settings to filter the content it offers, even though it doesn’t provide configurations for these or any other settings. Subscribe to [`$effectiveMaximumTVShowRating`](managedsettingsstore/$effectivemaximumtvshowrating.md) or [`$effectiveMaximumMovieRating`](managedsettingsstore/$effectivemaximummovierating.md) to determine what TV shows or movies to offer.

## Topics

### Creating the store
- [init()](managedsettingsstore/init.md)
  Creates a new instance of a store.
### Managing a settings group
- [protocol ManagedSettingsGroup](managedsettingsgroup.md)
  A group of settings to manage.
### Restricting device settings
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
### Filtering media content
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
### Restricting web content
- [var safari: SafariSettings](managedsettingsstore/safari.md)
  Settings that affect Safari’s search results and cookie policies.
- [struct SafariSettings](safarisettings.md)
  Constraints on Safari’s AutoFill and cookie behaviors.
- [var webContent: WebContentSettings](managedsettingsstore/webcontent.md)
  Settings that affect web content.
- [struct WebContentSettings](webcontentsettings.md)
  An object that configures which websites a user can access.
### Accessing metadata
- [struct BoundedSettingMetadata](boundedsettingmetadata.md)
  Additional information about a bounded setting.
- [struct SettingMetadata](settingmetadata.md)
  Additional information about a configurable setting.
### Observing current settings
- [var effectiveMaximumMovieRating: Int](managedsettingsstore/effectivemaximummovierating.md)
  The movie rating constraint that is active on this device.
- [var $effectiveMaximumTVShowRating: Published<Int>.Publisher](managedsettingsstore/$effectivemaximumtvshowrating.md)
### Structures
- [ManagedSettingsStore.Name](managedsettingsstore/name.md)
  The unique name of a store.
- [ManagedSettingsStore.TokenExpiryMessage](managedsettingsstore/tokenexpirymessage.md)
  A message that is posted in NotificationCenter when ManagedSettingsStore tokens are expired
### Initializers
- [convenience init(named: ManagedSettingsStore.Name)](managedsettingsstore/init(named:).md)
  Creates a new instance of a store with a custom name.
### Instance Properties
- [var $effectiveDenyExplicitContent: Published<Bool>.Publisher](managedsettingsstore/$effectivedenyexplicitcontent.md)
- [var $effectiveMaximumMovieRating: Published<Int>.Publisher](managedsettingsstore/$effectivemaximummovierating.md)
- [var effectiveDenyExplicitContent: Bool](managedsettingsstore/effectivedenyexplicitcontent.md)
  The deny explicit content constraint that is active on this device.
- [var isActive: Bool](managedsettingsstore/isactive.md)
  Property that controls whether the store is active
### Instance Methods
- [func clearAllSettings()](managedsettingsstore/clearallsettings.md)
  Clears all settings for this store.
- [func deleteStore()](managedsettingsstore/deletestore.md)
  Deletes this store
### Type Properties
- [static var stores: Set<ManagedSettingsStore.Name>](managedsettingsstore/stores.md)
  Get the name of all the stores configured by your app
### Type Methods
- [static func deleteStores(Set<ManagedSettingsStore.Name>)](managedsettingsstore/deletestores(_:).md)
  Deletes the given stores configured by your app if they exist
- [static func refresh(inout [ActivityCategoryToken]) throws](managedsettingsstore/refresh(_:)-4v4xe.md)
  Refresh expired ActivityCategoryTokens
- [static func refresh(inout [ApplicationToken]) throws](managedsettingsstore/refresh(_:)-65mti.md)
  Refresh expired ApplicationTokens
- [static func refresh(inout [WebDomainToken]) throws](managedsettingsstore/refresh(_:)-s5s3.md)
  Refresh expired WebDomainTokens

## Relationships

### Conforms To
- [ObservableObject](../Combine/ObservableObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore)*