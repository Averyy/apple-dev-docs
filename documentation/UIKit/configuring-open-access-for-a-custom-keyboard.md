# Configuring open access for a custom keyboard

**Framework**: UIKit

Enable network access and write access to a shared group container.

#### Overview

Custom keyboards operate in a sandboxed environment running in an isolated process. This sandbox’s default configuration disallows access to the network and prevents writing to the containing app’s shared group containers (reading is permitted). Open access lets you do things like store keyboard configuration, perform more complex analysis on text the user typed, or provide advanced features that require server support.

By setting the [`RequestsOpenAccess`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) flag to [`true`](https://developer.apple.com/documentation/swift/true) in your keyboard’s `Info.plist`, you can enable these features. Users must explicitly allow your keyboard to have open access by turning the “Allow Full Access” switch on for your keyboard in Settings.

> ❗ **Important**:  Enabling open access shouldn’t be done lightly. Keyboards handle some of the most sensitive user data. See [`Gain user trust`](configuring-open-access-for-a-custom-keyboard#Gain-user-trust.md) below.

 Enabling open access shouldn’t be done lightly. Keyboards handle some of the most sensitive user data. See [`Gain user trust`](configuring-open-access-for-a-custom-keyboard#Gain-user-trust.md) below.

##### Determine Whether You Need Open Access

Give careful consideration to whether you truly need open access or not. Although open access makes many things possible for a custom keyboard, it also increases your responsibilities. Consider the following lists describing the capabilities and privacy considerations with open access enabled or disabled.

With [`RequestsOpenAccess`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) set to [`false`](https://developer.apple.com/documentation/swift/false), or if the user has disallowed full access for your keyboard in Settings, users know that keystrokes go only to the app that’s currently using the keyboard. The system guarantees this by enabling the following capabilities and restrictions for the keyboard:

- Ability to perform all the normal duties expected of a basic keyboard
- Access to a common words lexicon for autocorrect and text suggestion
- Access to the text shortcuts list in Settings
- No access to the file system apart from the keyboard’s own sandbox container, and read-only access to containing app’s shared containers
- No access to microphone and speaker
- No ability to participate directly or indirectly in iCloud, Game Center, or In-App Purchase

However, with [`RequestsOpenAccess`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) set to [`true`](https://developer.apple.com/documentation/swift/true), users must explicitly allow your keyboard to have open access. They do this in Settings by selecting Allow Full Access for your keyboard. When they enable this, they know their keystrokes are available to the keyboard developer. The system enables the following capabilities and restrictions for open access keyboards:

- The open access keyboard has all the capabilities in the preceding list.
- The keyboard can access Location Services and Contacts, with user permission.
- The keyboard and containing app can employ a shared container.
- The keyboard can send keystrokes and other input events for server- side processing.
- The keyboard can use iCloud to ensure settings and the autocorrect lexicon are up to date on all devices.
- Through the containing app, the keyboard can participate in Game Center and In-App Purchase.
- If the keyboard supports mobile device management (MDM), it can work with managed apps.

> ❗ **Important**:  Open access keyboards must adhere to networked keyboard guidelines in App Store Review Guidelines and iOS Developer Program License Agreement. See the [`App Review Support`](https://developer.apple.comhttps://developer.apple.com/support/app-store/) page for more information.

 Open access keyboards must adhere to networked keyboard guidelines in App Store Review Guidelines and iOS Developer Program License Agreement. See the [`App Review Support`](https://developer.apple.comhttps://developer.apple.com/support/app-store/) page for more information.

You can determine whether your keyboard has open access by using the [`hasFullAccess`](uiinputviewcontroller/hasfullaccess.md) property on [`UIInputViewController`](uiinputviewcontroller.md).

##### Gain User Trust

The following table describes areas that are especially important for establishing and maintaining user trust.

|  |  |
| --- | --- |
| Safety of keystroke data | Users want their keystrokes to go to the document or text field they’re typing into, and not to be archived on a server or used for purposes that aren’t obvious to them. |
| Appropriate and minimal use of other user data | If your keyboard employs other user data, such as from Location Services or the Contacts database, the burden is on you to explain and demonstrate the benefit to your users. |

If you build a keyboard without open access, the system ensures that keystrokes can’t be sent back to your server or anywhere else. Use a non-networked keyboard if your goal is to provide normal keyboard functionality. Because of its restricted sandbox, a non-networked keyboard gives you a head start in meeting Apple’s data privacy guidelines and in gaining user trust.

Each keyboard capability associated with open access carries responsibilities on your part as a developer, as indicated in the next table. In general, treat user data with the greatest possible respect and don’t use it for any purpose that isn’t obvious to the user.

|  |  |  |
| --- | --- | --- |
| Shared container with containing app |  | Store data securely, and use only for the purpose of text input |
| Sending keystroke data to your server |  | Transmit data securely, and use only for the purpose of text input |
| Dynamic autocorrect lexicon based on network supplied data | Names of people, places, and current events in the news added to autocorrection lexicon | Don’t associate the user’s identity with their use of trending or other network- based information, for any reason that isn’t obvious to the user. |
| Address Book access | Names, places, and phone numbers relevant to the user added to autocorrection lexicon | Don’t use Address Book data for any purpose that isn’t obvious to the user. |
| Location Services access | Nearby place names added to autocorrection lexicon | Don’t use Location Services in the background. Don’t send location data to your servers for any purpose that isn’t obvious to the user. |

An open access keyboard and its containing app can send keystroke data to your server, which enables you to apply your computing resources to features like touch-event processing and input prediction. If you employ this capability, don’t store received keystroke or voice data beyond the time needed to provide text back to the user or to provide features that you explain to the user.

## See Also

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)
  Design a flexible, functional, and responsive interface for editing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/configuring-open-access-for-a-custom-keyboard)*