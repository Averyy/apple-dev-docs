# TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS

**Framework**: Technotes

Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.

#### Overview

The IMAP protocol defined in [`RFC 3501`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc3501.html) (IMAP4rev1) is one of the protocols used by Mail for iOS, iPadOS, and visionOS to connect to email servers.

To improve efficiency and performance for both the Mail app and email servers, the Mail app supports various extensions to the IMAP protocol. This document is intended for IMAP email server implementers to guide decisions on which extensions to support. For example, the `CONDSTORE`, `IDLE`, and `ESEARCH` extensions are especially important for efficient synchronization.

#### Details

Below are the IMAP extensions that Mail for iOS, iPadOS, and visionOS uses, with descriptions of their implementation.

| RFC | Capability / Name | Description |
| --- | --- | --- |
| [`RFC 3501`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc3501.html) | Pipelining | The Mail app uses pipelining to enqueue multiple IMAP commands with the server. Commands can be completed out-of-order and responses can be sent interleaved. |
| [`RFC 3501`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc3501.html) | `STARTTLS` | The Mail app upgrades plaintext connections using `STARTTLS`. Implicit TLS is generally preferred over `STARTTLS`, though, since it reduces connection setup time. |
| [`RFC 3501`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc3501.html) | Authentication | The Mail app uses either `LOGIN` or SASL `CRAM-MD5`/`PLAIN` authentication, based on server capabilities (`LOGINDISABLED`, `AUTH=PLAIN`, `AUTH=CRAM-MD5`). |
| [`RFC 4959`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc4959.html) | `SASL-IR` | The Mail app has to do fewer round trips during SASL authentication when the server supports `SASL-IR`. |
| [`RFC 7889`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc7889.html) | `APPENDLIMIT` | The Mail app supports both mailbox-specific and global append limits. If the server announces a corresponding `APPENDLIMIT` capability, the Mail app will not attempt to `APPEND` messages larger than this limit. |
| [`RFC 4978`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc4978.html) | `COMPRESS` | If the server announces the `COMPRESS=DEFLATE` capability, the Mail app enables compression to reduce bandwidth usage. Data sent to the server is compressed at level 1 for commands and at level 5 for messages. |
| [`RFC 4551`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc4551.html) | `CONDSTORE` | The Mail app uses `CONDSTORE` to efficiently retrieve changes to message flags. Without this capability, the Mail app falls back to re-fetching flags for all messages. |
| [`RFC 4731`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc4731.html) | `ESEARCH` | This reduces data size of responses when the Mail app sends `UID SEARCH` commands. The Mail app will send result options such as `RETURN (ALL)` for all `UID SEARCH` commands, such that the response from the server can use a more compact format for UIDs. |
| [`RFC 2971`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc2971.html) | `ID` | When the server supports this capability, the Mail app identifies itself to the server, and it allows the server to identify itself to the Mail app. |
| [`RFC 2177`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc2177.html) | `IDLE` | Enables efficient server updates for the currently selected mailbox. The Mail app applies these updates directly, often avoiding the need to re-sync the mailbox and allowing users to see updates almost immediately. If the server does not support `IDLE`, the Mail app may poll the server for changes at regular intervals. |
| [`RFC 5819`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc5819.html) | `LIST-STATUS` | The Mail app will use this to retrieve status as part of running the `LIST` command. If the server does not support `LIST-STATUS`, the Mail app may run `STATUS` for each mailbox in the list of mailboxes. |
| [`RFC 7888`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc7888.html) | `LITERAL+`/`LITERAL-` | The Mail app supports both extensions to reduce required round-trips. |
| [`RFC 6851`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc6851.html) | `MOVE` | The Mail app will use this to efficiently move messages between mailboxes. This notably improves message deletion, as messages are generally moved to Trash when the user deletes them. |
| [`RFC 6154`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc6154.html) | `SPECIAL-USE` | The Mail app honors `SPECIAL-USE` mailboxes during initial account setup, but lets users override mailbox assignments. |
| [`RFC 4315`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc4315.html) | `UIDPLUS` | The Mail app will use UIDs returned as part of `APPEND` and `MOVE` commands to improve efficiency. This notably affects uploading drafts and deleting messages (see `MOVE`). |
| [`RFC 9586`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9586.html) | `UIDONLY` | `UIDONLY` mode can substantially reduce resource requirements for some server implementations, since no message sequence numbers are used, and the server doesn’t have to map between UIDs and sequence numbers. The Mail app will send an `ENABLE UIDONLY` command to enable `UIDONLY` mode if the server announces all of the `PARTIAL`, `UIDBATCHES`, `ENABLE`, `UIDONLY`, and `ESEARCH` capabilities. |
| [`RFC 9394`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9394.html) | `PARTIAL` | When performing server-side search initiated by the user searching for messages, the Mail app will use [`RFC 9394`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9394.html) to limit the number of results requested if the server announced `PARTIAL` support. |
| [`UIDBATCHES`](https://developer.apple.comhttps://datatracker.ietf.org/doc/draft-ietf-mailmaint-imap-uidbatches/) | `UIDBATCHES` | The Mail app operates on roughly equally sized batches of messages for many operations. If the server supports `UIDBATCHES`, the client will use this extension to divide the messages in a particular mailbox into these batches. Otherwise, the Mail app will fall back to using `UID SEARCH` using message sequence numbers. |
| [`RFC 9738`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc9738.html) | `MESSAGELIMIT` | As noted under `UIDBATCHES`, the Mail app operates on batches of messages. The server can use `MESSAGELIMIT` to lower the size of these batches if the server is constrained. |

#### Revision History

-  First published.

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
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3191-imap-extensions-supported-by-mail)*