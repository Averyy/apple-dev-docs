# App services

**Framework**: Bundle Resources

Configure services provided by the app, like support for giving directions or using game controllers.

#### Overview

Add keys to your app’s [`Information Property List`](information-property-list.md) file that tell the system about services that your app provides.

## Topics

### Accessibility
- [MusicHapticsSupported](information-property-list/musichapticssupported.md)
  A Boolean value that indicates to the system that your app supports the Music Haptics feature.
### Accessories
- [NSAccessorySetupSupports](information-property-list/nsaccessorysetupsupports.md)
  An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.
- [NSAccessorySetupBluetoothCompanyIdentifiers](information-property-list/nsaccessorysetupbluetoothcompanyidentifiers.md)
  An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- [NSAccessorySetupBluetoothNames](information-property-list/nsaccessorysetupbluetoothnames.md)
  An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.
- [NSAccessorySetupBluetoothServices](information-property-list/nsaccessorysetupbluetoothservices.md)
  An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.
### Ad attributions
- [AdNetworkIdentifiers](information-property-list/adnetworkidentifiers.md)
  An array of strings that identifies the ad networks a publisher app shows advertisements for.
- [AttributionCopyEndpoint](information-property-list/attributioncopyendpoint.md)
  A key that defines a URL that AdAttributionKit uses to deliver copies of ad attribution postbacks.
- [EligibleForAdAttributionKitReengagementPostbackCopies](information-property-list/eligibleforadattributionkitreengagementpostbackcopies.md)
  A Boolean value that indicates whether the developer receives copies of AdAttributionKit reengagement postbacks.
### AlarmKit
- [NSAlarmKitUsageDescription](information-property-list/nsalarmkitusagedescription.md)
  A message that tells people why the app is requesting access to schedule alarms.
### Alterantive app marketplaces
- [MKSellsDigitalGoods](information-property-list/mksellsdigitalgoods.md)
  A Boolean value that indicates whether an alternative distribution app sells digital goods or services.
### Alternative browser engines
- [BEEmbeddedWebBrowserEngine](information-property-list/beembeddedwebbrowserengine.md)
  A string name of the alternative browser engine that your app embeds.
- [BEEmbeddedWebBrowserEngineVersion](information-property-list/beembeddedwebbrowserengineversion.md)
  A string version number for the alternative browser engine that your app embeds.
### Always On display
- [WKSupportsAlwaysOnDisplay](information-property-list/wksupportsalwaysondisplay.md)
  A Boolean value that determines whether the system displays the app in the Always On state.
### Authentication
- [ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn](information-property-list/asaccountauthenticationmodificationoptoutofsecuritypromptsonsignin.md)
  A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.
- [ASWebAuthenticationSessionWebBrowserSupportCapabilities](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities.md)
  A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.
### CallKit
- [NSVoIPUsageDescription](information-property-list/nsvoipusagedescription.md)
  A message that tells people why your app receives voice-over-IP (VoIP) calls in the background.
### Core spotlight
- [CoreSpotlightActions](information-property-list/corespotlightactions.md)
  A dictionary that contains details about actions available to users for Spotlight search results.
### Exposure notification
- [ENAPIVersion](information-property-list/enapiversion.md)
  A number that specifies the version of the API to use.
- [ENDeveloperRegion](information-property-list/endeveloperregion.md)
  A string that specifies the region that the app supports.
### External accessories
- [UIApplicationSupportsPrintCommand](information-property-list/uiapplicationsupportsprintcommand.md)
  A Boolean value that indicates whether the app supports the Command-P keyboard shortcut.
- [UISupportedExternalAccessoryProtocols](information-property-list/uisupportedexternalaccessoryprotocols.md)
  The protocols that the app uses to communicate with external accessory hardware.
### Games
- [AVGameBypassSystemSpatialAudio](information-property-list/avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](information-property-list/gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GCSupportedGameControllers](information-property-list/gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCSupportsControllerUserInteraction](information-property-list/gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCRequiresControllerUserInteraction](information-property-list/gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](information-property-list/gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](information-property-list/lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.
### Intents
- [INIntentsSupported](information-property-list/inintentssupported.md)
  The names of the intent classes your app handles directly.
- [INIntentsRestrictedWhileLocked](information-property-list/inintentsrestrictedwhilelocked.md)
  The names of the intent classes your app can’t handle when the user locks the device.
- [INIntentsRestrictedWhileProtectedDataUnavailable](information-property-list/inintentsrestrictedwhileprotecteddataunavailable.md)
  The names of the intent classes your app can’t handle when the user locks the device or the system blocks access to protected data.
- [INSupportedMediaCategories](information-property-list/insupportedmediacategories.md)
  Types of media supported by your app’s media-playing intents.
- [NSFocusStatusUsageDescription](information-property-list/nsfocusstatususagedescription.md)
  A message that tells people why your app requests access to a person’s focus status.
### Interprocess communication
- [XPCService](information-property-list/xpcservice.md)
### Live Activities
- [NSSupportsLiveActivities](information-property-list/nssupportsliveactivities.md)
  A Boolean value that indicates whether an app supports Live Activities.
- [NSSupportsLiveActivitiesFrequentUpdates](information-property-list/nssupportsliveactivitiesfrequentupdates.md)
  A Boolean value that indicates whether an app can update its Live Activities frequently.
### Maps
- [MKDirectionsApplicationSupportedModes](information-property-list/mkdirectionsapplicationsupportedmodes.md)
  The modes of transportation for which the app is capable of giving directions.
### Messages
- [NSStickerSharingLevel](information-property-list/nsstickersharinglevel.md)
- [NSCriticalMessagingUsageDescription](information-property-list/nscriticalmessagingusagedescription.md)
  A message that tells people why the app needs to send SMS messages.
### Network
- [NSApplicationServices](information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.
### Journaling Suggestions
- [JSNotificationURLFormat](information-property-list/jsnotificationurlformat.md)
  A universal link that determines how the system provides Journaling Suggestion notifications to your app.
### Safari services
- [SFSafariCorrespondingIOSAppBundleIdentifier](information-property-list/sfsafaricorrespondingiosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingIOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingiosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.
- [SFSafariCorrespondingMacOSAppBundleIdentifier](information-property-list/sfsafaricorrespondingmacosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingMacOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingmacosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.
### Sensors
- [SRResearchDataGeneration](information-property-list/srresearchdatageneration.md)
  A Boolean value that indicates whether use of an app contributes data to SensorKit while the user is enrolled in a health research study.
### Service management
- [SMAuthorizedClients](information-property-list/smauthorizedclients.md)
  The Service Management clients authorized to add and remove tools.
- [SMPrivilegedExecutables](information-property-list/smprivilegedexecutables.md)
  The Service Management tools owned by the app.
### StoreKit
- [SKAdNetworkItems](information-property-list/skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
- [SKExternalLinkAccount](information-property-list/skexternallinkaccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.
- [SKExternalPurchase](information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.
- [SKExternalPurchaseCustomLinkRegions](information-property-list/skexternalpurchasecustomlinkregions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [SKExternalPurchaseLink](information-property-list/skexternalpurchaselink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [SKExternalPurchaseMultiLink](information-property-list/skexternalpurchasemultilink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [SKIncludeConsumableInAppPurchaseHistory](information-property-list/skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.
- [SKExternalPurchaseLinkStreamingRegions](information-property-list/skexternalpurchaselinkstreamingregions.md)
  A list of country codes that indicate the regions where your music-streaming app communicates and promotes offers.
### User activities
- [NSUserActivityTypes](information-property-list/nsuseractivitytypes.md)
  The user activity types that the app supports.
### Wi-Fi Aware
- [WiFiAwareServices](information-property-list/wifiawareservices.md)
  Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.

## See Also

- [Protected resources](protected-resources.md)
  Control an app’s access to protected system services and user data.
- [Data and storage](data-and-storage.md)
  Regulate documents, URLs, and other kinds of data movement and storage.
- [Kernel and drivers](kernel-and-drivers.md)
  Configure device drivers provided by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-services)*