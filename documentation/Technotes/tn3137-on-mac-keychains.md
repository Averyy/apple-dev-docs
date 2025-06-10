# TN3137: On Mac keychain APIs and implementations

**Framework**: Technotes

Learn how the keychain on macOS differs from other Apple platforms.

#### Overview

All Apple platforms support the keychain.  On iOS, tvOS, and watchOS the keychain story is very simple: There’s a single SecItem API with consistent behavior.  This is not the case on macOS.  The keychain on macOS has a long history, dating back to the previous millenium.  This history, combined with a requirement to maintain compatibility with existing code, complicates the keychain’s design.  If you don’t understand that design, you may find some of its behavior surprising.

macOS has three keychain APIs:

- Keychain. This originated on traditional Mac OS.  Mac OS X supported it as a compatibility measure, and that support persists all the way through to the latest versions of macOS.
- SecKeychain. This was introduced with Mac OS X and was the standard macOS keychain API until the introduction of the SecItem API.
- SecItem. This was part of the original iOS SDK.  macOS gained support for it in macOS 10.6.

> **Note**: The Keychain API is declared in `<KeychainCore.h>` within the Core Services framework.  The SecKeychain API is declared in `<Security/SecKeychain.h>`, `<Security/SecKeychainItem.h>`, and `<Security/SecKeychainSearch.h>`, all within the Security framework.  The SecItem API is declared in `<Security/SecItem.h>`, also within the Security framework.

macOS has two keychain implementations:

- File-based keychain
- Data protection keychain

The file-based keychain has its origins on traditional Mac OS.  The data protection keychain originated on iOS and came to macOS with the advent of iCloud Keychain on macOS 10.9.

> ❗ **Important**: iOS, tvOS, and watchOS only support the SecItem API with the data protection keychain implementation.

The Keychain and SecKeychain APIs always target the file-based keychain.  The SecItem API can target either implementation.  It defaults to targeting the file-based keychain.  To target the data protection keychain, set the [`kSecUseDataProtectionKeychain`](https://developer.apple.com/documentation/Security/kSecUseDataProtectionKeychain) attribute or the [`kSecAttrSynchronizable`](https://developer.apple.com/documentation/Security/kSecAttrSynchronizable) attribute to true.

The file-based keychain is on the road to deprecation.  It’s not officially deprecated, but some of the APIs surrounding it are.  For example, `SecKeychainCreate` was deprecated in the macOS 12 SDK.  Moreover, new features, like iCloud Keychain, require the data protection keychain.

#### Choosing the Right Keychain

Choosing a keychain API is easy: Use the SecItem API.  If you have existing code that uses the older Keychain or SecKeychain APIs, consider updating it to use the SecItem API as part of your ongoing maintenance work.

Choosing a keychain implementation is more nuanced.  Default to targeting the data protection keychain because:

- It behaves consistently across all Apple platforms.
- It benefits from new features, like iCloud Keychain.
- It has an access control model that’s both easier to understand and better aligned with current platform norms.

In some environments your only option is the data protection keychain, including:

- Mac Catalyst apps
- iOS Apps on Mac

In these environments you don’t need to supply the `kSecUseDataProtectionKeychain` attribute or the `kSecAttrSynchronizable` attribute to target the data protection keychain.  It’s the default and only option.  The system ignores the `kSecUseDataProtectionKeychain` attribute in these environments.  If you have cross-platform keychain code, you may choose to simplify that code by setting `kSecUseDataProtectionKeychain` in all cases.

In other situations your only option is the file-based keychain:

- Programs that read existing items in a file-based keychain must target the file-based keychain.  If you find yourself in this situation, consider migrating items to the data protection keychain as you update your app.
- Programs that run outside of a user context, like a `launchd` daemon, must target the file-based keychain.  The data protection keychain is only available to programs running in a user context, like an app or an app extension.

#### Api Differences

The SecItem API is well aligned with the data protection keychain.  However, when you use it to target the file-based keychain it operates through a shim.  That shim has limitations.  Some of those limitations are inherent to the keychain implementation.  For example, the access control model of the file-based keychain is completely different than that of the data protection keychain, and the shim can’t make up for that.  However, some limitations are just bugs.  To avoid such problems, target the data protection keychain.  This is particularly important when you’re porting keychain code from iOS.

#### Implementation Differences

The data protection keychain is only available in a user login context.  You can’t use it, for example, from a `launchd` daemon.

Each user gets exactly one data protection keychain.  The system selects the correct keychain based on the context of the caller.  That’s why the data protection keychain is only available in a user login context.

File-based keychains are stored, as the name suggests, in files.  Every context has a keychain search list and a default keychain.  In a user context the search list includes a per-user  keychain and a single  keychain, with the former being the default.  In the system context the search list includes just the  keychain, which is also the default keychain.

When using the SecItem API to target the file-based keychain:

- [`SecItemAdd(_:_:)`](https://developer.apple.com/documentation/Security/SecItemAdd(_:_:)) adds the item to the default keychain.  Use [`kSecUseKeychain`](https://developer.apple.com/documentation/Security/kSecUseKeychain) to override this.
- Queries, like those done using [`SecItemCopyMatching(_:_:)`](https://developer.apple.com/documentation/Security/SecItemCopyMatching(_:_:)), consult all keychains in the search list.   Use [`kSecMatchSearchList`](https://developer.apple.com/documentation/Security/kSecMatchSearchList) to override this.

Each keychain implementation uses its own access control model:

- The file-based keychain uses access control lists (`SecAccess`).
- The data protection keychain uses keychain access groups, supplemented by an optional access control object ([`SecAccessControl`](https://developer.apple.com/documentation/Security/SecAccessControl)).

macOS builds the list of data protection keychain access groups available to your program from its code signing entitlements.  For the details, see [`Sharing access to keychain items among a collection of apps`](https://developer.apple.com/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps).  These entitlements must be authorized by a provisioning profile.  Your program needs an app-like bundle structure in which to embed that profile.  This is standard for app and app extensions but not for command-line tools.  For information on how to wrap a command-line tool in a dummy app-like structure, see [`Signing a daemon with a restricted entitlement`](https://developer.apple.com/documentation/Xcode/signing-a-daemon-with-a-restricted-entitlement).

> ❗ **Important**: This command-line tool will only work when run from a user context because, regardless of the packaging, the data protection keychain is only available in that context.

If you’re building library code, its data protection keychain access is determined by the entitlements of the host process’s main executable.

For more on provisioning profiles, see [`TN3125: Inside Code Signing: Provisioning Profiles`](tn3125-inside-code-signing-provisioning-profiles.md).

The data protection keychain can hold all keychain item classes (Internet password, generic password, certificate, key).  macOS 11 and later synchronize all classes; earlier versions synchronize only the password classes.

Some keychain features require the data protection keychain, including:

- iCloud Keychain.  See the [`kSecAttrSynchronizable`](https://developer.apple.com/documentation/Security/kSecAttrSynchronizable) attribute.
- Protecting an item with biometrics (Touch ID and Face ID).  See [`Restricting keychain item accessibility`](https://developer.apple.com/documentation/Security/restricting-keychain-item-accessibility).
- Protecting a key with the Secure Enclave.  See [`Protecting keys with the Secure Enclave`](https://developer.apple.com/documentation/Security/protecting-keys-with-the-secure-enclave).

#### User Interface

The Keychain Access application supports both file-based keychains and the data protection keychain.  The keychain list shows all the file-based keychains in the search list for the current user—typically this is just  and —and the data protection keychain.  It displays the latter as either  or , depending on whether the user has enabled iCloud Keychain.  To create, add, and remove a file-based keychain, choose the corresponding command on the File menu.

Keychain Access displays all keychain items in file-based keychains but only password items in the data protection keychain.

Keychain Access sometimes fails to reflect changes made to the keychain by other apps (r. 82556933).  If you see unexpected results, quit and relaunch Keychain Access.

The keychain support in the `security` command-line tool is primarily focused on the file-based keychain.

#### Revision History

-  Republished as TN3137.  Made significant editorial changes.
-  First published as ”On Mac Keychains” on Apple Developer Forums.

## See Also

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
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains)*