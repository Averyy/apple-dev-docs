# TN3111: iOS Wi-Fi API overview

**Framework**: Technotes

Explore the various Wi-Fi APIs available on iOS and their expected use cases.

#### Overview

iOS does not have a general-purpose API for Wi-Fi scanning and configuration.  However, it does support a wide range of special-purpose Wi-Fi APIs.  This technote lists some use cases supported by those special-purpose APIs.

While the focus of this technote is iOS, these APIs are also available on iPadOS.

#### Navigate an Internet Hotspot

If your app helps the user navigate an internet hotspot — a Wi-Fi network where the user must interact with the network to gain access to the wider internet — adopt the [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper) API.

To use `NEHotspotHelper` you must first be granted a special entitlement (`com.apple.developer.networking.HotspotHelper`) by Apple.  For information on how to apply for this, see [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper).

> ❗ **Important**: `NEHotspotHelper` is  useful for hotspot integration. There are both technical and business restrictions that prevent it from being used for other tasks, such as accessory integration or Wi-Fi based location.

iOS 26 introduced support for hotspot helper app extensions.  Adopt these to improve the efficiency, reliability, and privacy of your hotspot helper app.

#### Add an Accessory to the Users Network

If you’re creating a hardware accessory and you want to make it easy for the user to add it to their local network, your best option is to build your accessory with that in mind.  Use one of these approaches:

- Wireless Accessory Configuration (WAC) — The user can configure a WAC-capable accessory directly in Settings.  Optionally, use [`EAWiFiUnconfiguredAccessoryBrowser`](https://developer.apple.com/documentation/ExternalAccessory/EAWiFiUnconfiguredAccessoryBrowser) to integrate accessory configuration directly in your app.
- HomeKit — Call `HMHome` APIs like [`performAccessorySetup(using:completionHandler:)`](https://developer.apple.com/documentation/HomeKit/HMAccessorySetupManager/performAccessorySetup(using:completionHandler:)) to ask the system to scan for, pair, and configure any unpaired HomeKit accessories .

> ❗ **Important**: To add WAC or HomeKit support to your accessory, join the [`MFi Program`](https://developer.apple.comhttps://mfi.apple.com/).

If your accessory does not support WAC or HomeKit, you can build an accessory configuration experience on top of `NEHotspotConfigurationManager`, although this will not be as seamless as the WAC and HomeKit accessory experience.  For an example of how you might approach this, see [`Configuring a Wi-Fi accessory to join a network`](https://developer.apple.com/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network).

#### Temporarily Join a Network

If your app needs to temporarily join a Wi-Fi network — for example, you want to interact with a Wi-Fi enabled accessory with its own independent network — use `NEHotspotConfigurationManager` and set [`joinOnce`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfiguration/joinOnce) to true.  For more details, see [`Wi-Fi configuration`](https://developer.apple.com/documentation/NetworkExtension/wi-fi-configuration).

If you’re working with a Wi-Fi accessory, use [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) to simplify discovery and configuration of your accessory.

#### Permanently Join a Network

Some apps need to configure the iOS device to permanently join a Wi-Fi network, as if the user had selected the network in Settings > Wi-Fi.  For example, an app from an ISP might do this to get the user’s iOS device on to the Wi-Fi network published by a new DSL gateway that they’ve just installed.  If your app needs to do this, use `NEHotspotConfigurationManager` and set [`joinOnce`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfiguration/joinOnce) to false.  For more details, see [`Wi-Fi configuration`](https://developer.apple.com/documentation/NetworkExtension/wi-fi-configuration).

#### Peer to Peer Networking

If your goal is to communicate with nearby devices and accessories without configuring a Wi-Fi network, you have two options:

- Wi-Fi Aware™ (also known as Neighbor Awareness Networking or NAN)
- Apple peer-to-peer Wi-Fi

iOS introduced support for Wi-Fi Aware in iOS 26.  It’s supported on iPhone 12 and later.  See the [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) framework documentation for more details.

Wi-Fi Aware is an industry standard specification, opening up the possibility of communicating with non-Apple devices and accessories.

Apple peer-to-peer Wi-Fi dates all the way back to iOS 7.  It works on all iOS, iPadOS, macOS, tvOS, and visionOS devices.  For information about networking APIs that support Apple peer-to-peer Wi-Fi, see [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md).

> **Note**: A common misconception is that Multipeer Connectivity is the only way to use Apple peer-to-peer Wi-Fi. That’s not the case.  See [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md) for the full story.

Apple peer-to-peer Wi-Fi is not documented for third-party use, so this mechanism only works between Apple devices.

#### Location Tracking

If you’d like to use Wi-Fi data to determine the device’s location, use Core Location.  This locates the device using a wide variety of techniques, including Wi-Fi.  For more information, see [`Maps and Location`](https://developer.apple.comhttps://developer.apple.com/maps/).

#### Current Wi Fi Network

If you need to know the name of the device’s current Wi-Fi network, call [`fetchCurrent(completionHandler:)`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotNetwork/fetchCurrent(completionHandler:)).  That method requires iOS 14 or later.  On older systems, call [`CNCopyCurrentNetworkInfo`](https://developer.apple.com/documentation/SystemConfiguration/CNCopyCurrentNetworkInfo).

#### Revision History

-  Added information about hotspot helper app extensions and Wi-Fi Aware, both new in iOS 26.
-  Added information about AccessorySetupKit.  Added a link to TN3151.  Made other minor editorial changes.
-  Made minor editorial changes.
-  Republished as TN3111.  Broke the content into task-focused sections.  Added a link to [`Configuring a Wi-Fi accessory to join a network`](https://developer.apple.com/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network).  Added a reference to [`fetchCurrent(completionHandler:)`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotNetwork/fetchCurrent(completionHandler:)).  Updated the text for the new publication platform.
-  Added information about `NEHotspotConfigurationManager`.
-  First published as QA1942 ”iOS Wi-Fi Management APIs”.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3111-ios-wifi-api-overview)*