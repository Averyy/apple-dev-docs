# App and system extensions

**Framework**: Technology Overviews

Extend the reach of your app to other parts of the system.

Apps let people experience your content within the interface you create, but sometimes people want that same content outside of your app. For example, someone using a weather app might want to see the forecast on their iPhone Lock Screen or on the face of their Apple Watch. If your server generates notifications with images, you might want people to see those images in the system’s notification interface. You deliver these types of features using app extensions.

An *app extension* is a separate bundle that ships as part of your app and vends your app’s services to other parts of the system. Because app extensions are separate from your app, the system can launch and run them separately from your app. Some app extensions have an interface that the system displays, but many app extensions simply provide information for the system to use. For example, a Spotlight Import app extension indexes the content in one of your app’s custom file types.

## Choose an app extension

iOS, iPadOS, macOS, tvOS, visionOS, and watchOS support app extensions for specific features like sharing, Notification Center, or Safari. When you [add an app extension](../Xcode/configuring-a-new-target-in-your-project.md) to your existing app project, Xcode creates the initial code and resources and updates your project’s build settings. When you build your app, Xcode builds the app extension automatically and copies it to your [app bundle](./files-and-directories.md#Bundles).

| Extension point | Description | iOS/iPadOS | macOS | tvOS | visionOS | watchOS |
| --- | --- | --- | --- | --- | --- | --- |
| [Accessory Setup Extension](../DeviceDiscoveryExtension/DeviceDiscoveryExtension.md) | Configure third-party media receivers that your app uses to stream audio and video content. | ✅ |  |  |  |  |
| [Account Authentication](../AuthenticationServices/upgrading-account-security-with-an-account-authentication-modification-extension.md) | Automatically upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple. | ✅ |  |  |  |  |
| [Action Extension](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Action.html#//apple_ref/doc/uid/TP40014214-CH13-SW1) | Add custom actions to the share sheet to invoke your app’s functionality from any app. | ✅ | ✅ |  |  |  |
| [App Intents Extension](../AppIntents/app-intents.md) | Perform tasks associated with your app’s declared app intents. | ✅ | ✅ |  | ✅ | ✅ |
| [Audio Unit Extension](../AudioToolbox/AudioToolbox.md) | Create and modify audio in any app that uses sound, including music production apps such as GarageBand or Logic Pro X. | ✅ | ✅ |  | ✅ |  |
| [Authentication Services](https://developer.apple.com/videos/play/tech-talks/301/) | Streamline authentication for users by enabling single sign-on. | ✅ | ✅ |  | ✅ |  |
| [AutoFill Credential Provider](../AuthenticationServices/ascredentialproviderviewcontroller.md) | Surface credentials from your app in Password Autofill and pull your app’s password data into the Password AutoFill workflow. | ✅ | ✅ |  | ✅ |  |
| [Background Delivery Extension](../FinanceKit/FinanceKit.md) | Update the on-device financial data your app manages in the background. | ✅ |  |  |  |  |
| [Background Download](../BackgroundAssets/BackgroundAssets.md) | Download important assets shortly after app installation. | ✅ | ✅ | ✅ | ✅ |  |
| [Broadcast Setup UI Extension](../ReplayKit/ReplayKit.md) | Display the UI for a broadcast you start using ReplayKit. | ✅ | ✅ | ✅ | ✅ |  |
| [Broadcast Upload Extension](../ReplayKit/rpbroadcastsamplehandler.md) | Broadcast content that ReplayKit captures from your app. | ✅ | ✅ | ✅ | ✅ |  |
| [Call Directory Extension](../CallKit/CallKit.md) | Display caller identification from your appʼs custom contact list so users know who’s calling. | ✅ |  |  | ✅ |  |
| [Capture Extension](../LockedCameraCapture/LockedCameraCapture.md) | Lets people launch your app’s camera experience from the Lock Screen, Control Center, or the Action button. | ✅ |  |  |  |  |
| [ClassKit Context Provider](../ClassKit/clscontextprovider.md) | Update the status of your appʼs activities so that status is visible in the Schoolwork app. | ✅ | ✅ |  | ✅ |  |
| [Contact Provider Extension](../ContactProvider/contactproviderextension.md) | Provide contact items to the system-wide Contacts ecosystem. | ✅ |  |  |  |  |
| [Content Blocker Extension](../SafariServices/creating-a-content-blocker.md) | Provide rules for hiding elements, blocking loads, and stripping cookies from Safari requests. | ✅ | ✅ |  | ✅ |  |
| [Core Spotlight Delegate](../CoreSpotlight/regenerating-your-app-s-indexes-on-demand.md) | Regenerate your app’s search indexes in response to system-initiated maintenance requests. | ✅ | ✅ |  | ✅ |  |
| [Custom Keyboard Extension](../UIKit/creating-a-custom-keyboard.md) | Provide systemwide customized text input for unique input methods or specific languages. | ✅ |  |  |  |  |
| [Device Activity Monitor Extension](../DeviceActivity/deviceactivitymonitor.md) | Detect and warn about excessive time spent on app and website activities. | ✅ |  |  |  |  |
| [Device Activity Report Extension](../UIKit/creating-a-custom-keyboard.md) | Receive and display device-activity information in a privacy-friendly way. | ✅ |  |  |  |  |
| [File Provider Extension](../FileProvider/FileProvider.md) | Let other apps access the documents and directories stored and managed by your app. | ✅ | ✅ |  | ✅ |  |
| [File Provider UI Extension](../FileProviderUI/FileProviderUI.md) | Add custom actions to the document browserʼs context menu for documents that your app manages. | ✅ |  |  |  |  |
| [File System Extension](../FSKit/FSKit.md) | Provide the implementation for a custom file system. |  | ✅ |  |  |  |
| [Finder Sync](../FinderSync/FinderSync.md) | Keep files in sync with a back-end storage service. |  | ✅ |  |  |  |
| [Hotspot Authentication](../NetworkExtension/nehotspotauthenticationprovider.md) | Authenticate the current device on a Wi-Fi hotspot. | ✅ |  |  |  |  |
| [Hotspot Evaluation](../NetworkExtension/nehotspotevaluationprovider.md) | Evaluate the available Wi-Fi hotspots in a privacy-friendly way. | ✅ |  |  |  |  |
| [Identity Document Provider](../IdentityDocumentServicesUI/IdentityDocumentServicesUI.md) | Validates the digital credentials that your app manages. | ✅ |  |  |  |  |
| [iMessage Extension](../Messages/Messages.md) | Allow users to send text, stickers, media files, and interactive messages. | ✅ |  |  |  |  |
| [Intents Extension](../SiriKit/creating-an-intents-app-extension.md) | Let users interact with your app using Siri. | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Intents UI Extension](../SiriKit/creating-an-intents-ui-extension.md) | Customize the interface for interactions with your app in Siri conversations or Maps. | ✅ |  |  | ✅ |  |
| [Live Caller ID Lookup Extension](../IdentityLookup/getting-up-to-date-calling-and-blocking-information-for-your-app.md) | Provide caller ID and call-blocking services from a server you maintain. Available in iOS only. | ✅ |  |  |  |  |
| [Location Push Service Extension](../CoreLocation/creating-a-location-push-service-extension.md) | Enable a location sharing app – with a user’s authorization – to query a user’s location in response to a push from Apple Push Notification service (APNs). | ✅ |  |  |  |  |
| [Mail](../MailKit/meextension.md) | Enhance Mail by adding custom actions, blocking content, signing and encoding messages, and more. |  | ✅ |  |  |  |
| [Matter Extension](../MatterSupport/adding-matter-support-to-your-ecosystem.md) | Perform required configuration of a newly added Matter device. | ✅ | ✅ |  | ✅ |  |
| [Media Device Discovery](../DeviceDiscoveryExtension/dddiscoveryextension.md) | Discover third-party media receivers that your app can use to stream audio and video content. | ✅ |  |  | ✅ |  |
| [Media Extension](../MediaExtension/MediaExtension.md) | Support media assets that the system doesn’t support natively. |  | ✅ |  |  |  |
| [Message Filter Extension](../IdentityLookup/IdentityLookup.md) | Identify and filter unwanted SMS and MMS messages. | ✅ |  |  | ✅ |  |
| [Network Extension](../NetworkExtension/NetworkExtension.md) | Provide system-level networking services such as VPN, proxies, or content filtering. | ✅ | ✅ | ✅ | ✅ |  |
| [Notification Content Extension](../UserNotificationsUI/customizing-the-appearance-of-notifications.md) | Customize the appearance of your app’s notification alerts. | ✅ | ✅ |  | ✅ |  |
| [Notification Service Extension](../UserNotifications/modifying-content-in-newly-delivered-notifications.md) | Modify the payload of a remote notification before it’s displayed on the user’s device. | ✅ | ✅ |  | ✅ | ✅ |
| [Persistent Token Extension](../CryptoTokenKit/authenticating-users-with-a-cryptographic-token.md) | Grant access to user accounts and the keychain using a token. | ✅ | ✅ |  | ✅ |  |
| [Photo Editing Extension](../PhotoKit/creating-photo-editing-extensions.md) | Allow your app to edit assets directly within the Photos app. | ✅ | ✅ |  |  |  |
| [Photo Project Extension](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md) | Augment the macOS Photos app with extensions that support project creation. |  | ✅ |  |  |  |
| [Print Service Extension](../UIKit/uiprintserviceextension.md) | Locate and set up an AirPrint printer and make it available as a printer destination. | ✅ |  |  | ✅ |  |
| [Quick Look Preview Extension](../QuickLook/QuickLook.md) | Provide previews of documents your app owns so they can be viewed in any app. | ✅ | ✅ |  |  |  |
| [Safari Extension](../SafariServices/SafariServices.md) | Extend the web-browsing experience in Safari by leveraging web technologies and native code. | ✅ | ✅ |  | ✅ |  |
| [Share Extension](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html#//apple_ref/doc/uid/TP40014214-CH12-SW1) | Let users post to your social-network service from any app. | ✅ | ✅ |  |  |  |
| [Shield Action Extension](../ManagedSettings/shieldactiondelegate.md) | Manage the system’s response to shield actions, which hide the content of apps and websites. | ✅ |  |  |  |  |
| [Shield Configuration](../ManagedSettingsUI/ManagedSettingsUI.md) | Customize the appearance of shields to match the style of your app. | ✅ |  |  |  |  |
| [Smart Card Token Extension](../CryptoTokenKit/authenticating-users-with-a-cryptographic-token.md) | Grant access to user accounts and the keychain using a hardware-based token. |  | ✅ |  |  |  |
| [Spotlight Import Extension](../CoreSpotlight/csimportextension.md) | Make content in your app searchable in Spotlight, Safari, Siri, and more. | ✅ | ✅ |  | ✅ |  |
| [Sticker Pack Extension](../Messages/Messages.md) | Add custom stickers to Messages. | ✅ |  |  |  |  |
| [Thumbnail Extension](../QuickLookThumbnailing/providing-thumbnails-of-your-custom-file-types.md) | Display thumbnails of your custom document types in all apps. | ✅ | ✅ |  | ✅ |  |
| [TV Top Shelf](../TVServices/TVServices.md) | Help users discover your app by providing Top Shelf content and a description of your tvOS app. |  |  | ✅ |  |  |
| [Unwanted Communication](../IdentityLookup/sms-and-call-spam-reporting.md) | Block incoming phone calls using your app’s custom unsolicited caller database. | ✅ |  |  | ✅ |  |
| [URL Filter Network](../NetworkExtension/neurlfiltercontrolprovider.md) | Filter URLs using an on-device data set or an off-device server. | ✅ |  |  |  |  |
| [Virtual Conference](../EventKit/ekvirtualconferenceprovider.md) | Integrate your video conferencing service directly into events on user’s calendars. | ✅ | ✅ |  | ✅ |  |
| [Widget Extension](../WidgetKit/creating-a-widget-extension.md) | Show relevant, glanceable content from your app on the iOS Home Screen and Lock Screen, macOS Notification Center, and as complications in watchOS. | ✅ | ✅ |  | ✅ | ✅ |
| [Xcode Source Editor](../XcodeKit/creating-a-source-editor-extension.md) | Provide custom editing features directly inside Xcode’s source editor. |  | ✅ |  |  |  |

## Share data with your app

The system runs app extensions as separate processes, so they don’t automatically share your app’s resources or permissions. Configure your app extension to run independently whenever possible. If you must share data between your app and app extension, [create an App Group](../Xcode/configuring-app-groups.md) and give access to both processes.

## Host custom extensions from your app

If your app supports contributions from outside apps, you can define your own app extensions and run them in a safe environment using the [ExtensionFoundation](../ExtensionFoundation/ExtensionFoundation.md) framework. Custom app extensions are a way for you to add new capabilities to your app. For example, a graphics editing app might support new types of filters or visual effects. If your app lets app extensions provide a custom interface, the [ExtensionKit](../ExtensionKit/ExtensionKit.md) framework helps you present that interface securely.

## Implement low-level services using system extensions

Create a system extension to add low-level capabilities that previously required modifications to the system kernel. Apple devices support the following types of system extensions:

- [Network extensions](../NetworkExtension/NetworkExtension.md) specify a system’s network configuration, create VPNs, filter network content, manage DNS configurations, and more.
- [Endpoint security extensions](../EndpointSecurity/EndpointSecurity.md) monitor system events for malicious activity and provide a response.
- [DriverKit extensions](./hardware-level-interactions.md#Build-drivers-to-support-custom-hardware-features) communicate with connected hardware devices.

In macOS, use the [System Extensions](../SystemExtensions/SystemExtensions.md) framework to install and upgrade system extensions. In iPadOS, the system automatically discovers and upgrades system extensions. Because system extensions modify system behaviors, they must contain appropriate entitlements so the system can verify the extension is genuine. [Install extensions](../SystemExtensions/installing-system-extensions-and-drivers.md) when your app first runs to make them available to the system.

> ❗ **Important**: Build system extensions with extra care, and test your code thoroughly before deploying it to customer devices. Although the code itself runs in user space, bugs in your code can prevent people from accessing important features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/app-extensions)*