# Entitlements

**Framework**: Bundle Resources  
**Kind**: struct

Key-value pairs that grant an executable permission to use a service or technology.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

An  is a right or privilege that grants an executable particular capabilities. For example, an app needs the [`HomeKit Entitlement`](entitlements/com.apple.developer.homekit.md) — along with explicit user consent — to access a user’s home automation network. An app stores its entitlements as key-value pairs embedded in the code signature of its binary executable.

You configure entitlements for your app by declaring capabilities for a target in Xcode, see [`Capabilities`](https://developer.apple.com/documentation/Xcode/capabilities). Xcode records capabilities that you add in a property list file with the `.entitlements` extension. You can also edit the entitlements file directly. When code signing your app, Xcode combines the entitlements file, information from your developer account, and other project information to apply a final set of entitlements to your app.

## Topics

### Essentials
- [Diagnosing Issues with Entitlements](diagnosing-issues-with-entitlements.md)
  Verify your app’s entitlements at every stage of development to track down errors during distribution.
- [Signing a daemon with a restricted entitlement](../Xcode/signing-a-daemon-with-a-restricted-entitlement.md)
  Wrap a daemon in an app-like structure to use an entitlement thatʼs authorized by a provisioning profile.
### Alternative marketplaces
- [com.apple.developer.marketplace.app-installation](entitlements/com.apple.developer.marketplace.app-installation.md)
  The entitlement that enables an app to vend other apps as an alternative app marketplace.
### App Clips
- [Parent Application Identifiers Entitlement](entitlements/com.apple.developer.parent-application-identifiers.md)
  A list of parent application identifiers for an App Clip with exactly one entry.
- [com.apple.developer.associated-appclip-app-identifiers](entitlements/com.apple.developer.associated-appclip-app-identifiers.md)
  A list of App Clip identifiers for an app with exactly one entry.
- [com.apple.developer.on-demand-install-capable](entitlements/com.apple.developer.on-demand-install-capable.md)
  A Boolean value that indicates whether a bundle represents an App Clip.
### Authentication
- [AutoFill Credential Provider Entitlement](entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md)
  A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
- [Sign in with Apple Entitlement](entitlements/com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.
### CallKit
- [Default Calling App](entitlements/com.apple.developer.calling-app.md)
  A Boolean value that indicates whether an app can be the default calling app on someone’s device.
### CarPlay
- [com.apple.developer.carplay-audio](entitlements/com.apple.developer.carplay-audio.md)
- [com.apple.developer.carplay-charging](entitlements/com.apple.developer.carplay-charging.md)
- [com.apple.developer.carplay-communication](entitlements/com.apple.developer.carplay-communication.md)
- [com.apple.developer.carplay-maps](entitlements/com.apple.developer.carplay-maps.md)
- [com.apple.developer.carplay-parking](entitlements/com.apple.developer.carplay-parking.md)
- [com.apple.developer.carplay-quick-ordering](entitlements/com.apple.developer.carplay-quick-ordering.md)
- [com.apple.developer.carplay-messaging](entitlements/com.apple.developer.carplay-messaging.md)
- [com.apple.developer.playable-content](entitlements/com.apple.developer.playable-content.md)
### Contacts
- [com.apple.developer.contacts.notes](entitlements/com.apple.developer.contacts.notes.md)
  A Boolean value that indicates whether the app may access the notes in contact entries.
### Device Management
- [com.apple.developer.automated-device-enrollment.add-devices](entitlements/com.apple.developer.automated-device-enrollment.add-devices.md)
  A Boolean value that indicates whether an app may add a device to Automated Device Enrollment.
### Education
- [ClassKit Environment Entitlement](entitlements/com.apple.developer.classkit-environment.md)
  The ClassKit development or production environment for an education app that works with the Schoolwork app.
- [com.apple.developer.automatic-assessment-configuration](entitlements/com.apple.developer.automatic-assessment-configuration.md)
  A Boolean value that indicates whether an app may create an assessment session.
### Email clients
- [com.apple.developer.mail-client](entitlements/com.apple.developer.mail-client.md)
  A Boolean that indicates whether the app can act as a user’s default email client.
### Enterprise
- [Apple Neural Engine access](entitlements/com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
- [Increased performance headroom](entitlements/com.apple.developer.app-compute-category.md)
  An entitlement that allows an app to adjust thresholds that balance thermal dissipation and performance against fan noise and other factors.
- [Passthrough in screen capture](entitlements/com.apple.developer.screen-capture.include-passthrough.md)
  A Boolean value that indicates whether an app can include passthrough in screen capture.
- [Main camera access](entitlements/com.apple.developer.arkit.main-camera-access.allow.md)
  A Boolean value that indicates whether an app can use ARKit to access the main cameras on Apple Vision Pro.
- [Object-tracking parameter adjustment](entitlements/com.apple.developer.arkit.object-tracking-parameter-adjustment.allow.md)
  A Boolean value that allows an app to use ARKit to track more objects with a higher frequency.
- [Spatial barcode and QR code scanning](entitlements/com.apple.developer.arkit.barcode-detection.allow.md)
  A Boolean value that indicates whether an app can use ARKit to detect, position, and decode barcode and QR codes.
- [UVC Device Access on visionOS](entitlements/com.apple.developer.avfoundation.uvc-device-access.md)
  A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.
### Exposure notification
- [com.apple.developer.exposure-notification](entitlements/com.apple.developer.exposure-notification.md)
  A Boolean value that indicates whether the app may use exposure notification.
### Family controls
- [Family Controls](entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.
### File provider
- [com.apple.developer.fileprovider.testing-mode](entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.
### Games
- [Game Center Entitlement](entitlements/com.apple.developer.game-center.md)
  A Boolean value that indicates whether users of the app may see and compare achievements on a leaderboard, invite friends, and start multiplayer games.
### Group activities
- [com.apple.developer.group-session](entitlements/com.apple.developer.group-session.md)
  A Boolean value that indicates whether the app may implement shared group experiences.
### Health
- [HealthKit Entitlement](entitlements/com.apple.developer.healthkit.md)
  A Boolean value that indicates whether the app may request user authorization to access health and activity data that appears in the Health app.
- [HealthKit Capabilities Entitlement](entitlements/com.apple.developer.healthkit.access.md)
  Health data types that require additional permission.
- [com.apple.developer.healthkit.background-delivery](entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [com.apple.developer.healthkit.recalibrate-estimates](entitlements/com.apple.developer.healthkit.recalibrate-estimates.md)
  A Boolean value that determines whether your app can recalibrate the prediction algorithm used to calculate supported sample types.
### Home automation
- [HomeKit Entitlement](entitlements/com.apple.developer.homekit.md)
  A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- [Matter Allow Setup Payload](entitlements/com.apple.developer.matter.allow-setup-payload.md)
  A Boolean value that allows an app to provide an optional Matter Setup payload while setting up a Matter device in an ecosystem.
### Hypervisor
- [com.apple.security.hypervisor](entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.vm.networking](entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.security.virtualization](entitlements/com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.
### iCloud
- [com.apple.developer.icloud-container-development-container-identifiers](entitlements/com.apple.developer.icloud-container-development-container-identifiers.md)
  The container identifiers for the iCloud development environment.
- [com.apple.developer.icloud-container-environment](entitlements/com.apple.developer.icloud-container-environment.md)
  The development or production environment to use for the iCloud containers.
- [iCloud Container Identifiers Entitlement](entitlements/com.apple.developer.icloud-container-identifiers.md)
  The container identifiers for the iCloud production environment.
- [iCloud Services Entitlement](entitlements/com.apple.developer.icloud-services.md)
  The iCloud services used by the app.
- [iCloud Key-Value Store Entitlement](entitlements/com.apple.developer.ubiquity-kvstore-identifier.md)
  The container identifier to use for iCloud key-value storage.
### Journaling Suggestions
- [com.apple.developer.journal.allow](entitlements/com.apple.developer.journal.allow.md)
  The entitlement that enables an app to present the journaling suggestions picker.
### Location
- [com.apple.developer.location.push](entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
### Managed App Distribution
- [Managed App Installation UI](entitlements/com.apple.developer.managed-app-distribution.install-ui.md)
  An entitlement you enable so your app can use Managed App Distribution.
### Media
- [Media Device Discovery Extension](entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.
- [com.apple.developer.coremotion.head-pose](entitlements/com.apple.developer.coremotion.head-pose.md)
  An entitlement that enables someone’s head movement to determine the orientation of spatialized sound output.
- [com.apple.developer.spatial-audio.profile-access](entitlements/com.apple.developer.spatial-audio.profile-access.md)
  An entitlement that enables your app to use the personalized spatial audio profile.
- [com.apple.developer.avfoundation.multitasking-camera-access](entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md)
  A Boolean value that indicates whether an app may continue using the camera at the same time as another foreground app.
### Memory
- [com.apple.developer.kernel.increased-memory-limit](entitlements/com.apple.developer.kernel.increased-memory-limit.md)
  A Boolean value that indicates whether core features of your app may perform better with a higher memory limit on supported devices.
- [Extended Virtual Addressing Entitlement](entitlements/com.apple.developer.kernel.extended-virtual-addressing.md)
  A Boolean value that indicates whether the app may access an extended address space.
### Metal
- [com.apple.developer.sustained-execution](entitlements/com.apple.developer.sustained-execution.md)
  A Boolean value that indicates whether your app performs consistently when the system constrains it to a sustainable performance level.
### Messages
- [Critical Messaging](entitlements/com.apple.developer.messages.critical-messaging.md)
  A Boolean value that indicates whether an app can use the Critical Messaging API to send SMS messages.
- [Default Messaging App](entitlements/com.apple.developer.messaging-app.md)
  A Boolean value that indicates whether an app can be the default messaging app on someone’s device.
### MessageUI
- [com.apple.developer.upi-device-validation](entitlements/com.apple.developer.upi-device-validation.md)
  A Boolean value that indicates whether the app can use Unified Payments Interface (UPI) device enrollment.
### Navigation
- [Default Navigation](entitlements/com.apple.developer.navigation-app.md)
  A Boolean value that indicates whether an app can be the default navigation app on someone’s device.
### Networking
- [Network Extensions Entitlement](entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Personal VPN Entitlement](entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
- [Associated Domains Entitlement](entitlements/com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
- [com.apple.developer.networking.multicast](entitlements/com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
- [com.apple.developer.associated-domains.applinks.read-write](entitlements/com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](entitlements/com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](entitlements/com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)
### Notifications
- [APS Environment Entitlement](entitlements/aps-environment.md)
  The environment for push notifications.
- [APS Environment (macOS) Entitlement](entitlements/com.apple.developer.aps-environment.md)
  The environment for push notifications in macOS apps.
- [com.apple.developer.usernotifications.filtering](entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.
### Privacy
- [com.apple.developer.device-information.user-assigned-device-name](entitlements/com.apple.developer.device-information.user-assigned-device-name.md)
  The entitlement for accessing the user-assigned device name instead of a generic device name.
### Push to talk
- [Push to Talk Entitlement](entitlements/com.apple.developer.push-to-talk.md)
### SafetyKit
- [com.apple.developer.severe-vehicular-crash-event](entitlements/com.apple.developer.severe-vehicular-crash-event.md)
  The entitlement for accessing Crash Detection events.
### SecureElementCredential
- [com.apple.developer.secure-element-credential](entitlements/com.apple.developer.secure-element-credential.md)
  A Boolean value that indicates whether your app can use the SecureElementCredential framework.
- [com.apple.developer.secure-element-credential.default-contactless-app](entitlements/com.apple.developer.secure-element-credential.default-contactless-app.md)
  A Boolean value that indicates whether your app that uses the SecureElementCredential framework can become the default contactless app.
### Security
- [App Sandbox](../Security/app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
- [Camera entitlement](entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
- [Address book entitlement](entitlements/com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [com.apple.security.files.user-selected.read-only](entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.
- [com.apple.security.files.downloads.read-write](entitlements/com.apple.security.files.downloads.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Downloads folder.
- [com.apple.security.assets.pictures.read-only](entitlements/com.apple.security.assets.pictures.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Pictures folder.
- [com.apple.security.assets.pictures.read-write](entitlements/com.apple.security.assets.pictures.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Pictures folder.
- [com.apple.security.assets.music.read-only](entitlements/com.apple.security.assets.music.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Music folder.
- [com.apple.security.assets.music.read-write](entitlements/com.apple.security.assets.music.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Music folder.
- [com.apple.security.assets.movies.read-only](entitlements/com.apple.security.assets.movies.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Movies folder.
- [com.apple.security.assets.movies.read-write](entitlements/com.apple.security.assets.movies.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Movies folder.
- [Hardened Runtime](../Security/hardened-runtime.md)
  Manage security protections and resource access for your macOS apps.
- [Allow execution of JIT-compiled code entitlement](entitlements/com.apple.security.cs.allow-jit.md)
  A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)
  A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](entitlements/com.apple.security.cs.allow-dyld-environment-variables.md)
  A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Library Validation Entitlement](entitlements/com.apple.security.cs.disable-library-validation.md)
  A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Disable Executable Memory Protection Entitlement](entitlements/com.apple.security.cs.disable-executable-page-protection.md)
  A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](entitlements/com.apple.security.cs.debugger.md)
  A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.
- [Audio Input Entitlement](entitlements/com.apple.security.device.audio-input.md)
  A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.
- [Photos Library Entitlement](entitlements/com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.
- [App Groups Entitlement](entitlements/com.apple.security.application-groups.md)
  A list of identifiers specifying the groups your app belongs to.
- [Apple Events Entitlement](entitlements/com.apple.security.automation.apple-events.md)
  A Boolean value that indicates whether the app may prompt the user for permission to send Apple events to other apps.
- [Keychain Access Groups Entitlement](entitlements/keychain-access-groups.md)
  The identifiers for the keychain groups that the app may share items with.
- [Data Protection Entitlement](entitlements/com.apple.developer.default-data-protection.md)
  The level of data protection for sensitive user data when an app accesses it on a device.
- [App Attest Environment](entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.
- [com.apple.security.smartcard](entitlements/com.apple.security.smartcard.md)
  A Boolean that indicates whether your app has access to smart card slots and smart cards.
### Sensitive content analysis
- [com.apple.developer.sensitivecontentanalysis.client](entitlements/com.apple.developer.sensitivecontentanalysis.client.md)
  A code-signing entitlement that enables an app to detect nudity in images and video.
### Sensors
- [com.apple.developer.sensorkit.reader.allow](entitlements/com.apple.developer.sensorkit.reader.allow.md)
  The necessary entitlement to access sensor data that’s required by your app’s preapproved research study.
### Siri
- [Siri Entitlement](entitlements/com.apple.developer.siri.md)
  A Boolean value that indicates whether the app handles Siri requests.
### StoreKit
- [com.apple.developer.storekit.external-link.account](entitlements/com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [com.apple.developer.storekit.external-purchase](entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [com.apple.developer.storekit.external-purchase-link](entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
### System
- [DriverKit](driverkit.md)
  Develop device drivers in macOS and iPadOS.
- [System Extensions](system-extensions.md)
  Extend the capabilities of macOS from user space.
### Translation
- [Translation](entitlements/com.apple.developer.translation-app.md)
  A Boolean value that indicates whether an app can be the default translation app on someone’s device.
### TV
- [User Management Entitlement](entitlements/com.apple.developer.user-management.md)
  The entitlement for distinguishing between multiple user accounts on Apple TV.
- [com.apple.developer.video-subscriber-single-sign-on](entitlements/com.apple.developer.video-subscriber-single-sign-on.md)
  A Boolean value that indicates whether your app can use the TV Provider Authentication service.
- [com.apple.smoot.subscriptionservice](entitlements/com.apple.smoot.subscriptionservice.md)
  A Boolean value that indicates whether your app can integrate with APIs to provide different feed based content.
### Wallet
- [Pass Type IDs Entitlement](entitlements/com.apple.developer.pass-type-identifiers.md)
  A list of identifiers that specify pass types that your app can access in Wallet.
- [Merchant IDs Entitlement](entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](entitlements/com.apple.developer.in-app-identity-presentment.md)
- [com.apple.developer.in-app-identity-presentment.merchant-identifiers](entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers.md)
- [ID Verifier - Display Only](entitlements/com.apple.developer.proximity-reader.identity.display.md)
- [ID Verifier - Data Transfer](entitlements/com.apple.developer.proximity-reader.identity.read.md)
### WeatherKit
- [WeatherKit Entitlement](entitlements/com.apple.developer.weatherkit.md)
  A Boolean value that indicates whether the app may use WeatherKit.
### Web browsers
- [com.apple.developer.web-browser](entitlements/com.apple.developer.web-browser.md)
  A Boolean that indicates whether the app can act as the user’s default web browser.
- [com.apple.developer.web-browser.public-key-credential](entitlements/com.apple.developer.web-browser.public-key-credential.md)
  A Boolean value that lets your app make registration and assertion requests for passkeys and security keys for any relying party identifier.
- [com.apple.developer.browser.app-installation](entitlements/com.apple.developer.browser.app-installation.md)
  The entitlement that enables a browser to install alternative-distribution apps from a website.
### Wireless interfaces
- [Access Wi-Fi Information Entitlement](entitlements/com.apple.developer.networking.wifi-info.md)
  A Boolean value indicating whether your app can access information about the connected Wi-Fi network.
- [Wireless Accessory Configuration Entitlement](entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [Multipath Entitlement](entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
- [Hotspot Configuration Entitlement](entitlements/com.apple.developer.networking.hotspotconfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
- [Near Field Communication Tag Reader Session Formats Entitlement](entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.
- [com.apple.developer.nfc.hce](entitlements/com.apple.developer.nfc.hce.md)
  A Boolean value indicating whether your app can use the card session API.
- [com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes](entitlements/com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes.md)
  An array of identifier strings the app handles with the card session API.
- [com.apple.developer.nfc.hce.default-contactless-app](entitlements/com.apple.developer.nfc.hce.default-contactless-app.md)
  A Boolean value indicating whether your app can be a default app for contactless NFC with the card session API.
### Deprecated entitlements
- [Maps Entitlement](entitlements/com.apple.developer.maps.md)
  A Boolean value that indicates whether the app may provide directions beyond what Maps supports, such as subway routes, hiking trails, and bike paths.
- [Inter-App Audio Entitlement](entitlements/inter-app-audio.md)
  A Boolean value that indicates whether the app may exchange audio with other Inter-App Audio-enabled apps.
- [All files entitlement](entitlements/com.apple.security.files.all.md)
  A Boolean value that indicates whether the app may have access to all files.
### BrowserEngineKit
- [com.apple.developer.embedded-web-browser-engine](entitlements/com.apple.developer.embedded-web-browser-engine.md)
- [com.apple.developer.memory.transfer_accept](entitlements/com.apple.developer.memory.transfer_accept.md)
- [com.apple.developer.memory.transfer_send](entitlements/com.apple.developer.memory.transfer_send.md)
- [com.apple.developer.web-browser-engine.host](entitlements/com.apple.developer.web-browser-engine.host.md)
- [com.apple.developer.web-browser-engine.networking](entitlements/com.apple.developer.web-browser-engine.networking.md)
- [com.apple.developer.web-browser-engine.rendering](entitlements/com.apple.developer.web-browser-engine.rendering.md)
- [com.apple.developer.web-browser-engine.webcontent](entitlements/com.apple.developer.web-browser-engine.webcontent.md)
### ScreenCaptureKit
- [Persistent Content Capture](entitlements/com.apple.developer.persistent-content-capture.md)
  A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.
### Type Aliases
- [com.apple.developer.accessibility.merchant-api-control](entitlements/com.apple.developer.accessibility.merchant-api-control.md)

## See Also

- [Information Property List](information-property-list.md)
  A resource containing key-value pairs that identify and configure a bundle.
- [Privacy manifest files](privacy-manifest-files.md)
  Describe the data your app or third-party SDK collects and the reasons required APIs it uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements)*