# TN3189: Managing Mail background traffic load

**Framework**: Technotes

Identify iOS Mail background traffic and manage its impact on your IMAP server.

#### Overview

To enhance the user experience, iOS Mail downloads a user’s email in the background. As part of a software update, some email data may require re-downloading. Since many devices will update at similar times, iOS Mail introduces a mechanism for IMAP email servers to limit concurrent downloads.

This process involves two main steps:

1.  [`RFC 3501`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3501) IMAP email servers can detect if a connection is for a background download. iOS Mail clients identify themselves to the server using the `ID` command. Starting with iOS 18.5, this command includes an `event` field. This field will indicate if the connection is being used for background downloading.
2.  If the server needs to limit its load and the client has been identified as a background download, the server should send a `NO [UNAVAILABLE]` tagged response to the `ID` command. This will result in the background download being postponed approximately a day, after which the client will retry the download.

#### Identify Background Traffic From Mail

Starting with iOS 18.5, the [`RFC 2971`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2971) `ID` command includes an `event` field. The value of this field is either `NIL` or a list of comma-separated identifiers.

The server should only consider the `event` field value if the email client identifies itself with a `name` field that has a `com.apple.` prefix. For example, `"name" "com.apple.email.maild"` indicates that this is the the Mail app.

If the comma-separated identifiers of the `event` field include either:

- `indexer`, or
- `back-fill`,

it indicates that the connection is being used for background downloading.

> **Note**: The event field may contain other identifiers, either by themselves or as a list of comma-separated identifiers. The server should ignore all identifiers except `indexer` and `back-fill`. Allowing for other identifiers supports extension without affecting IMAP email servers’ ability to detect background downloading.

The `event` field could take on values such as:

- `periodic`
- `periodic,push`
- `NIL`

These would  indicate a background download. However, values such as:

- `back-fill`
- `periodic,back-fill`
- `back-fill,periodic`
- `indexer`

would indicate background download activity because they include `indexer` or `back-fill`.

Here’s an example interaction between the client (C) and server (S):

```None
C: A1 ID ("name" "com.apple.email.maild" "os" "iOS" "vendor" "Apple Inc" "event" NIL)
S: * ID ("name" "Mail Server" "version" "3")
S: A1 OK Completed
```

In this example, the client did include the `event` field, but its value is `NIL`. This is not a background download.

Here’s another example interaction:

```text
C: A1 ID ("name" "com.apple.email.search-indexer" "os" "iOS" "vendor" "Apple Inc" "event" "indexer")
S: * ID ("name" "Mail Server" "version" "3")
S: A1 OK Completed
```

In this case, the client indicated that it is performing a background download through the `indexer` value of the `event` field.

#### Tell Mail to Back Off

Since iOS Mail may use an already established connection to perform background activity, iOS Mail might send subsequent `ID` commands with updated `event` fields. These will always contain the full set of fields of the original `ID` command, notably the `name` and `event` field. These subsequent `ID` commands may include switching from non-background to background download.

The load shedding using `NO [UNAVAILABLE]` for background downloads lets IMAP email servers reduce peak load without a direct impact on user experience.

IMAP email servers should only send `NO [UNAVAILABLE]` when the Mail app has identified itself as Mail through the `name` field, and has indicated that it is doing background downloads through the `event` field as noted above.

Here’s an example of an interaction where the IMAP email server tell the Mail app to back off:

```text
C: A1 ID ("name" "com.apple.email.maild" "os" "iOS" "vendor" "Apple Inc" "event" "back-fill,periodic")
S: * ID ("name" "Mail Server" "version" "3")
S: A1 NO [UNAVAILABLE] Completed
```

Here the IMAP email server responds with a tagged response containing `NO` and the response code `UNAVAILABLE,` as defined in [`RFC 3501`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3501) and [`RFC 5530`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5530). This informs the iOS Mail app to back off, and it will close the connection.

> **Note**: Mail does not include an event field on macOS. It also doesn’t handle load shedding through the `NO [UNAVAILABLE]` server response.

#### Revision History

-  First published.

## See Also

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
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3189-managing-mail-background-traffic-load)*