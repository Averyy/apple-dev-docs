# App extensions

**Framework**: Technology Overviews

Extend the reach of your app to other parts of the system.

Apps let people experience your content within the interface you create, but sometimes people want that same content outside of your app. For example, someone using a weather app might want to see the forecast on their iPhone Lock Screen or on the face of their Apple Watch. If your server generates notifications with images, you might want people to see those images in the system’s notification interface. You deliver these types of features using app extensions.

An  is a separate bundle that ships as part of your app and vends your app’s services to other parts of the system. Because app extensions are separate from your app, the system can launch and run them separately from your app. Some app extensions have an interface that the system displays, but many app extensions simply provide information for the system to use. For example, a Spotlight Import app extension indexes the content in one of your app’s custom file types.

#### Choose an App Extension

iOS, iPadOS, macOS, tvOS, visionOS, and watchOS support app extensions for specific features like sharing, Notification Center, or Safari. When you [`Configuring a new target in your project`](https://developer.apple.com/documentation/Xcode/configuring-a-new-target-in-your-project) to your existing app project, Xcode creates the initial code and resources and updates your project’s build settings. When you build your app, Xcode builds the app extension automatically and copies it to your [`Bundles`](files-and-directories#Bundles.md).

| Extension point | Description | iOS/iPadOS | macOS | tvOS | visionOS | watchOS |
| --- | --- | --- | --- | --- | --- | --- |
| [`DeviceDiscoveryExtension`](https://developer.apple.com/documentation/DeviceDiscoveryExtension) | Configure third-party media receivers that your app uses to stream audio and video content. | ✅ |  |  |  |  |
| [`Upgrading Account Security With an Account Authentication Modification Extension`](https://developer.apple.com/documentation/AuthenticationServices/upgrading-account-security-with-an-account-authentication-modification-extension) | Automatically upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple. | ✅ |  |  |  |  |
| [`Action Extension`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Action.html#//apple_ref/doc/uid/TP40014214-CH13-SW1) | Add custom actions to the share sheet to invoke your app’s functionality from any app. | ✅ | ✅ |  |  |  |
| [`App intents`](https://developer.apple.com/documentation/AppIntents/app-intents) | Perform tasks associated with your app’s declared app intents. | ✅ | ✅ |  | ✅ | ✅ |
| [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox#Audio-Units) | Create and modify audio in any app that uses sound, including music production apps such as GarageBand or Logic Pro X. | ✅ | ✅ |  | ✅ |  |
| [`Authentication Services`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/301/) | Streamline authentication for users by enabling single sign-on. | ✅ | ✅ |  | ✅ |  |
| [`ASCredentialProviderViewController`](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderViewController) | Surface credentials from your app in Password Autofill and pull your app’s password data into the Password AutoFill workflow. | ✅ | ✅ |  | ✅ |  |
| [`FinanceKit`](https://developer.apple.com/documentation/FinanceKit) | Update the on-device financial data your app manages in the background. | ✅ |  |  |  |  |
| [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) | Download important assets shortly after app installation. | ✅ | ✅ | ✅ | ✅ |  |
| [`ReplayKit`](https://developer.apple.com/documentation/ReplayKit) | Display the UI for a broadcast you start using ReplayKit. | ✅ | ✅ | ✅ | ✅ |  |
| [`RPBroadcastSampleHandler`](https://developer.apple.com/documentation/ReplayKit/RPBroadcastSampleHandler) | Broadcast content that ReplayKit captures from your app. | ✅ | ✅ | ✅ | ✅ |  |
| [`CallKit`](https://developer.apple.com/documentation/CallKit) | Display caller identification from your appʼs custom contact list so users know who’s calling. | ✅ |  |  | ✅ |  |
| [`LockedCameraCapture`](https://developer.apple.com/documentation/LockedCameraCapture) | Lets people launch your app’s camera experience from the Lock Screen, Control Center, or the Action button. | ✅ |  |  |  |  |
| [`CLSContextProvider`](https://developer.apple.com/documentation/ClassKit/CLSContextProvider) | Update the status of your appʼs activities so that status is visible in the Schoolwork app. | ✅ | ✅ |  | ✅ |  |
| [`ContactProviderExtension`](https://developer.apple.com/documentation/ContactProvider/ContactProviderExtension) | Provide contact items to the system-wide Contacts ecosystem. | ✅ |  |  |  |  |
| [`Creating a content blocker`](https://developer.apple.com/documentation/SafariServices/creating-a-content-blocker) | Provide rules for hiding elements, blocking loads, and stripping cookies from Safari requests. | ✅ | ✅ |  | ✅ |  |
| [`Regenerating your app’s indexes on demand`](https://developer.apple.com/documentation/CoreSpotlight/regenerating-your-app-s-indexes-on-demand) | Regenerate your app’s search indexes in response to system-initiated maintenance requests. | ✅ | ✅ |  | ✅ |  |
| [`Creating a custom keyboard`](https://developer.apple.com/documentation/UIKit/creating-a-custom-keyboard) | Provide systemwide customized text input for unique input methods or specific languages. | ✅ |  |  |  |  |
| [`DeviceActivityMonitor`](https://developer.apple.com/documentation/DeviceActivity/DeviceActivityMonitor) | Detect and warn about excessive time spent on app and website activities. | ✅ |  |  |  |  |
| [`Creating a custom keyboard`](https://developer.apple.com/documentation/UIKit/creating-a-custom-keyboard) | Receive and display device-activity information in a privacy-friendly way. | ✅ |  |  |  |  |
| [`File Provider`](https://developer.apple.com/documentation/FileProvider) | Let other apps access the documents and directories stored and managed by your app. | ✅ | ✅ |  | ✅ |  |
| [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) | Add custom actions to the document browserʼs context menu for documents that your app manages. | ✅ |  |  |  |  |
| [`FSKit`](https://developer.apple.com/documentation/FSKit) | Provide the implementation for a custom file system. |  | ✅ |  |  |  |
| [`Finder Sync`](https://developer.apple.com/documentation/FinderSync) | Keep files in sync with a back-end storage service. |  | ✅ |  |  |  |
| [`NEHotspotAuthenticationProvider`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotAuthenticationProvider) | Authenticate the current device on a Wi-Fi hotspot. | ✅ |  |  |  |  |
| [`NEHotspotEvaluationProvider`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotEvaluationProvider) | Evaluate the available Wi-Fi hotspots in a privacy-friendly way. | ✅ |  |  |  |  |
| [`IdentityDocumentServicesUI`](https://developer.apple.com/documentation/IdentityDocumentServicesUI) | Validates the digital credentials that your app manages. | ✅ |  |  |  |  |
| [`Messages`](https://developer.apple.com/documentation/Messages) | Allow users to send text, stickers, media files, and interactive messages. | ✅ |  |  |  |  |
| [`Creating an Intents App Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension) | Let users interact with your app using Siri. | ✅ | ✅ | ✅ | ✅ | ✅ |
| [`Creating an Intents UI Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-ui-extension) | Customize the interface for interactions with your app in Siri conversations or Maps. | ✅ |  |  | ✅ |  |
| [`Getting up-to-date calling and blocking information for your app`](https://developer.apple.com/documentation/IdentityLookup/getting-up-to-date-calling-and-blocking-information-for-your-app) | Provide caller ID and call-blocking services from a server you maintain. Available in iOS only. | ✅ |  |  |  |  |
| [`Creating a location push service extension`](https://developer.apple.com/documentation/CoreLocation/creating-a-location-push-service-extension) | Enable a location sharing app – with a user’s authorization – to query a user’s location in response to a push from Apple Push Notification service (APNs). | ✅ |  |  |  |  |
| [`MEExtension`](https://developer.apple.com/documentation/MailKit/MEExtension) | Enhance Mail by adding custom actions, blocking content, signing and encoding messages, and more. |  | ✅ |  |  |  |
| [`Adding Matter support to your ecosystem`](https://developer.apple.com/documentation/MatterSupport/Adding-Matter-support-to-your-ecosystem) | Perform required configuration of a newly added Matter device. | ✅ | ✅ |  | ✅ |  |
| [`DDDiscoveryExtension`](https://developer.apple.com/documentation/DeviceDiscoveryExtension/DDDiscoveryExtension) | Discover third-party media receivers that your app can use to stream audio and video content. | ✅ |  |  | ✅ |  |
| [`MediaExtension`](https://developer.apple.com/documentation/MediaExtension) | Support media assets that the system doesn’t support natively. |  | ✅ |  |  |  |
| [`SMS and Call Reporting`](https://developer.apple.com/documentation/IdentityLookup) | Identify and filter unwanted SMS and MMS messages. | ✅ |  |  | ✅ |  |
| [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) | Provide system-level networking services such as VPN, proxies, or content filtering. | ✅ | ✅ | ✅ | ✅ |  |
| [`Customizing the Appearance of Notifications`](https://developer.apple.com/documentation/UserNotificationsUI/customizing-the-appearance-of-notifications) | Customize the appearance of your app’s notification alerts. | ✅ | ✅ |  | ✅ |  |
| [`Modifying content in newly delivered notifications`](https://developer.apple.com/documentation/UserNotifications/modifying-content-in-newly-delivered-notifications) | Modify the payload of a remote notification before it’s displayed on the user’s device. | ✅ | ✅ |  | ✅ | ✅ |
| [`Authenticating Users with a Cryptographic Token`](https://developer.apple.com/documentation/CryptoTokenKit/authenticating-users-with-a-cryptographic-token) | Grant access to user accounts and the keychain using a token. | ✅ | ✅ |  | ✅ |  |
| [`Creating Photo Editing Extensions`](https://developer.apple.com/documentation/PhotoKit/creating-photo-editing-extensions) | Allow your app to edit assets directly within the Photos app. | ✅ | ✅ |  |  |  |
| [`Creating a Slideshow Project Extension for Photos`](https://developer.apple.com/documentation/PhotoKit/creating-a-slideshow-project-extension-for-photos) | Augment the macOS Photos app with extensions that support project creation. |  | ✅ |  |  |  |
| [`UIPrintServiceExtension`](https://developer.apple.com/documentation/UIKit/UIPrintServiceExtension) | Locate and set up an AirPrint printer and make it available as a printer destination. | ✅ |  |  | ✅ |  |
| [`Quick Look`](https://developer.apple.com/documentation/QuickLook) | Provide previews of documents your app owns so they can be viewed in any app. | ✅ | ✅ |  |  |  |
| [`Safari Services`](https://developer.apple.com/documentation/SafariServices) | Extend the web-browsing experience in Safari by leveraging web technologies and native code. | ✅ | ✅ |  | ✅ |  |
| [`Share Extension`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html#//apple_ref/doc/uid/TP40014214-CH12-SW1) | Let users post to your social-network service from any app. | ✅ | ✅ |  |  |  |
| [`ShieldActionDelegate`](https://developer.apple.com/documentation/ManagedSettings/ShieldActionDelegate) | Manage the system’s response to shield actions, which hide the content of apps and websites. | ✅ |  |  |  |  |
| [`ManagedSettingsUI`](https://developer.apple.com/documentation/ManagedSettingsUI) | Customize the appearance of shields to match the style of your app. | ✅ |  |  |  |  |
| [`Authenticating Users with a Cryptographic Token`](https://developer.apple.com/documentation/CryptoTokenKit/authenticating-users-with-a-cryptographic-token) | Grant access to user accounts and the keychain using a hardware-based token. |  | ✅ |  |  |  |
| [`CSImportExtension`](https://developer.apple.com/documentation/CoreSpotlight/CSImportExtension) | Make content in your app searchable in Spotlight, Safari, Siri, and more. | ✅ | ✅ |  | ✅ |  |
| [`Messages`](https://developer.apple.com/documentation/Messages) | Add custom stickers to Messages. | ✅ |  |  |  |  |
| [`Providing Thumbnails of Your Custom File Types`](https://developer.apple.com/documentation/QuickLookThumbnailing/providing-thumbnails-of-your-custom-file-types) | Display thumbnails of your custom document types in all apps. | ✅ | ✅ |  | ✅ |  |
| [`TV Services`](https://developer.apple.com/documentation/TVServices) | Help users discover your app by providing Top Shelf content and a description of your tvOS app. |  |  | ✅ |  |  |
| [`SMS and Call Spam Reporting`](https://developer.apple.com/documentation/IdentityLookup/sms-and-call-spam-reporting) | Block incoming phone calls using your app’s custom unsolicited caller database. | ✅ |  |  | ✅ |  |
| [`NEURLFilterControlProvider`](https://developer.apple.com/documentation/NetworkExtension/NEURLFilterControlProvider) | Filter URLs using an on-device data set or an off-device server. | ✅ |  |  |  |  |
| [`EKVirtualConferenceProvider`](https://developer.apple.com/documentation/EventKit/EKVirtualConferenceProvider) | Integrate your video conferencing service directly into events on user’s calendars. | ✅ | ✅ |  | ✅ |  |
| [`Creating a widget extension`](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension) | Show relevant, glanceable content from your app on the iOS Home Screen and Lock Screen, macOS Notification Center, and as complications in watchOS. | ✅ | ✅ |  | ✅ | ✅ |
| [`Creating a Source Editor Extension`](https://developer.apple.com/documentation/XcodeKit/creating-a-source-editor-extension) | Provide custom editing features directly inside Xcode’s source editor. |  | ✅ |  |  |  |

#### Share Data with Your App

The system runs app extensions as separate processes, so they don’t automatically share your app’s resources or permissions. Configure your app extension to run independently whenever possible. If you must share data between your app and app extension, [`Configuring app groups`](https://developer.apple.com/documentation/Xcode/configuring-app-groups) and give access to both processes.

#### Host Custom Extensions in Your App

If your app supports contributions from outside apps, you can define your own app extensions and run them in a safe environment using the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework. Custom app extensions are a way for you to add new capabilities to your app. For example, a graphics editing app might support new types of filters or visual effects. If your app lets app extensions provide a custom interface, the [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework helps you present that interface securely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/app-extensions)*