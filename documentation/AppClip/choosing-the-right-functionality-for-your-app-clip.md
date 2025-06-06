# Choosing the right functionality for your App Clip

**Framework**: App Clips

Review frameworks available to App Clips and identify functionality that makes a great App Clip.

#### Overview

An App Clip is a lightweight version of your app that offers some of its functionality when and where it’s needed. It offers a focused feature set and is designed to launch instantly, protect user privacy, and preserve resources. As a result, an App Clip comes with some limitations. Before you create your App Clip, first review technology that’s available to App Clips and identify functionality that makes a great App Clip.

> **Note**:  Your full app can offer multiple App Clip experiences, but you have to package them as a single App Clip target. Additionally, the full app must include the same functionality as the App Clip.

 Your full app can offer multiple App Clip experiences, but you have to package them as a single App Clip target. Additionally, the full app must include the same functionality as the App Clip.

To ensure a fast launch experience, App Clips must be small:

- If you make your App Clip available on devices running iOS 15 and earlier, the uncompressed App Clip binary can be up to 10 MB in size.
- If you make your App Clip available on devices running iOS 16 and later, the uncompressed App Clip binary can be up to 15 MB in size.

If you make your App Clip available on devices running iOS 17 and later, the uncompressed App Clip binary can be up to 100 MB in size if it meets the following conditions:

- The App Clip only supports digital invocations — for example, from your website or Spotlight search — and not from physical invocations like App Clip Codes, QR codes, or NFC tags
- People use your App Clip in situations where a reliable internet connection is likely, for example, at home
- Your App Clip doesn’t support iOS versions prior to iOS 17

Aim to keep your App Clip well below the applicable limit. For more information, see [`Keep your App Clip small in size`](creating-an-app-clip-with-xcode#Keep-your-App-Clip-small-in-size.md).

##### Review Available Frameworks and Apis

App Clips make use of [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) and [`UIKit`](https://developer.apple.com/documentation/UIKit), and have access to the same frameworks as your full app. However, the following frameworks provide no functionality at runtime: [`App Intents`](https://developer.apple.com/documentation/AppIntents), [`Assets Library`](https://developer.apple.com/documentation/AssetsLibrary), [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks), [`CallKit`](https://developer.apple.com/documentation/CallKit), `CareKit`, [`Contacts`](https://developer.apple.com/documentation/Contacts), [`Contacts UI`](https://developer.apple.com/documentation/ContactsUI), [`Core Motion`](https://developer.apple.com/documentation/CoreMotion), [`EventKit`](https://developer.apple.com/documentation/EventKit), [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI), [`File Provider`](https://developer.apple.com/documentation/FileProvider), [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI), [`HealthKit`](https://developer.apple.com/documentation/HealthKit), [`HomeKit`](https://developer.apple.com/documentation/HomeKit), [`Media Player`](https://developer.apple.com/documentation/MediaPlayer), [`Messages`](https://developer.apple.com/documentation/Messages), [`Message UI`](https://developer.apple.com/documentation/MessageUI), [`Nearby Interaction`](https://developer.apple.com/documentation/NearbyInteraction), [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit), [`ResearchKit`](https://developer.apple.comhttps://researchkit.org), [`SensorKit`](https://developer.apple.com/documentation/SensorKit), and [`Speech`](https://developer.apple.com/documentation/Speech).

For most unavailable frameworks, using them in an App Clip doesn’t result in compile-time errors, but their APIs return values that indicate unavailability, empty data, or error codes at runtime. For example, HealthKit’s [`isHealthDataAvailable()`](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614180-ishealthdataavailable) returns `false` when you call it from an App Clip.

App Clips can’t perform background activity. For example, they can’t make use of the following functionality:

- Background networking with [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession)
- Functionality enabled by the Background Modes capability as described in [`Pushing background updates to your App`](https://developer.apple.com/documentation/UserNotifications/pushing-background-updates-to-your-app)
- The ability to maintain Bluetooth connections while the App Clip isn’t in use

Some frameworks are available to App Clips but offer only limited functionality, or using them requires special consideration:

Note that an App Clip may configure Wi-Fi networks using the [`Hotspot Configuration Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.HotspotConfiguration). Additionally, to connect to an authentication provider, it may initialize an [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession) using [`init(url:callback:completionHandler:)`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession/init(url:callback:completionHandler:)).

##### Preserve User Privacy

App Clips come with limitations that help to protect user privacy and prevent user tracking across apps and App Clips, for example:

- Functionality provided by [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) isn’t available.
- App Clips can’t request authorization to track a person with [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency).
- Both [`name`](https://developer.apple.com/documentation/UIKit/UIDevice/name) and [`identifierForVendor`](https://developer.apple.com/documentation/UIKit/UIDevice/identifierForVendor) return an empty string.
- App Clips can’t request continuous location access. However, you can call [`requestWhenInUseAuthorization()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/requestWhenInUseAuthorization()) to request the When In Use authorization, which resets automatically the next day at 4:00 a.m.
- In iOS 17 and later, App Clips can request the  [`Pass Type IDs Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.pass-type-identifiers) to read passes stored in the Wallet app. On devices that run iOS 16 or earlier, where your App Clip can’t read passes stored in the Wallet app, your App Clip can add a pass to the Wallet app and check if this pass is already present. For more information, see [`Checking Whether a Pass Is in the Library`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Apps.html#//apple_ref/doc/uid/TP40012195-CH6-SW3).
- An App Clip can’t share data with any other app except its corresponding full app. For more information, see [`Sharing data between your App Clip and your full app`](sharing-data-between-your-app-clip-and-your-full-app.md).

To help protect user data, they can’t access:

- Apple Music and Media
- Data from apps like Calendar, Contacts, Files, Health, Messages, Reminders, and Photos
- Motion and fitness data

##### Reserve Certain Functionality for Your Full App

App Clips provide an in-the-moment experience and focus on offering the quickest possible solution to an everyday task, so some functionality works best in your full app. Reserve the following functionality for the full app:

- App extensions
- Customization and settings, for example, creation of a settings bundle
- Data handoff and document opening
- In-app purchases
- Low-level UNIX functionality, for example, BSD notifications
- Multiple scenes on iPad
- On-demand resources
- Promoting other apps
- Registration of custom URL schemes
- Requests for reviews of the full app by using StoreKit’s [`requestReview(in:)`](https://developer.apple.com/documentation/StoreKit/SKStoreReviewController/requestReview(in:)) method
- Searching for paired Bluetooth devices


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip)*