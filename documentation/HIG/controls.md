---
url: https://developer.apple.com/design/human-interface-guidelines/controls
framework: HIG
---

# Controls

**Type:** article

**Platforms:** ios, ipados, macos

> **Updated 2024-06-10:** New page.

A control provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.

![A partial screenshot of controls in Control Center, such as the Airplane Mode toggle, Wi-Fi toggle, and AirPlay button. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/3eb51c82ce94c19b99ff18e912b90052/components-controls-intro~dark%402x.png)
A control is a button or toggle that provides quick access to your app’s features from other areas of the system. Control buttons perform an action, link to a specific area of your app, or launch a [Camera experiences on a locked device](controls.md#Camera-experiences-on-a-locked-device). Control toggles switch between two states, such as on and off.
People can add controls to Control Center by pressing and holding in an empty area of Control Center, to the Lock Screen by customizing their Lock Screen, and to the Action button by configuring the Action button in the Settings app.

## Anatomy
Controls contain a symbol image, a title, and, optionally, a value. The symbol visually represents what the control does and can be a symbol from [SF Symbols](sf-symbols.md) or a custom symbol. The title describes what the control relates to, and the value represents the state of the control. For example, the title can display the name of a light in a room, while the value can display whether it’s on or off.
![A diagram showing the placement of the symbol image, the title, and the value for a control toggle.](https://docs-assets.developer.apple.com/published/4db19a1800d82606bc42f3112ad208d9/control-medium-anatomy~dark%402x.png)
Controls display their information differently depending on where they appear:
- In Control Center, a control displays its symbol and, at larger sizes, its title and value.
- On the Lock Screen, a control displays its symbol.
- On iPhone devices with a control assigned to the Action button, pressing and holding it displays the control’s symbol in the Dynamic Island, as well as its value (if present).
![A partial screenshot of Control Center on iPhone, highlighting that the Silent mode control is active, with a symbol of a bell with a line drawn through it and red tint.](https://docs-assets.developer.apple.com/published/02ea9cd61e6ca7c226e049da08f50c4f/control-control-center~dark%402x.png)
![A partial screenshot of the bottom of the Lock Screen on iPhone, highlighting that the Silent mode control is active on the right, with a symbol of a bell with a line drawn through it and red tint.](https://docs-assets.developer.apple.com/published/3de4be33f6935c3f8fb50b29241da866/control-lock-screen~dark%402x.png)
![A partial screenshot that displays the Dynamic Island at the top of the Home Screen on iPhone, showing that the Silent mode control is active with a red tinted symbol of a bell with a line drawn through it in the leading area and red tinted text that says Silent in the trailing area.](https://docs-assets.developer.apple.com/published/8a8e0edf80ffe38ebb80702a1db3343d/control-dynamic-island~dark%402x.png)

## Best practices
**Offer controls for actions that provide the most benefit without having to launch your app.** For example, launching a Live Activity from a control creates an easy and seamless experience that informs someone about progress without having to navigate to your app to stay up to date. For guidance, see [Live Activities](live-activities.md).
**Update controls when someone interacts with them, when an action completes, or remotely with a push notification.** Update the contents of a control to accurately reflect the state and show if an action is still in progress.
**Choose a descriptive symbol that suggests the behavior of the control.** Depending on where a person adds a control, it may not display the title and value, so the symbol needs to convey enough information about the control’s action. For control toggles, provide a symbol for both the on and off states. For example, use the SF Symbols `door.garage.open` and `door.garage.closed` to represent a control that opens and closes a garage door. For guidance, see [SF Symbols](sf-symbols.md).
**Use symbol animations to highlight state changes.** For control toggles, animate the transition between both on and off states. For control buttons with actions that have a duration, animate indefinitely while the action performs and stop animating when the action is complete. For developer guidance, see [Symbols](../Symbols.md) and [SymbolEffect](../Symbols/SymbolEffect.md).
**Select a tint color that works with your app’s brand.** The system applies this tint color to a control toggle’s symbol in its on state. When a person performs the action of a control from the Action button, the system also uses this tint color to display the value and symbol in the Dynamic Island. For guidance, see [Branding](branding.md).
![An inactive control toggle with a light bulb symbol that isn't tinted.](https://docs-assets.developer.apple.com/published/1b418a5e8b38b4545baa6e4e322b3326/control-lightbulb-not-tinted~dark%402x.png)
![An active control toggle with a light bulb symbol that's tinted yellow.](https://docs-assets.developer.apple.com/published/78b45f8d64f92bcd7b2e3ca465dfcab7/control-lightbulb-tinted~dark%402x.png)
**Help people provide additional information the system needs to perform an action.** A person may need to configure a control to perform a desired action — for example, select a specific light in a house to turn on and off. If a control requires configuration, prompt people to complete this step when they first add it. People can reconfigure the control at any time. For developer guidance, see [promptsForUserConfiguration()](../SwiftUI/ControlWidgetConfiguration/promptsForUserConfiguration().md).
![A representation of a control with the ability to set an option to a value a person chooses.](https://docs-assets.developer.apple.com/published/19695cdb573954a9947e8143411fa231/control-configuration-options~dark%402x.png)
**Provide hint text for the Action button.** When a person presses the Action button, the system displays hint text to help them understand what happens when they press and hold. When someone presses and holds the Action button, the system performs the action configured to it. Use verbs to construct the hint text. For developer guidance, see [controlWidgetActionHint(_:)](../SwiftUI/View/controlWidgetActionHint(_:)-5yoyh.md).
![A partial screenshot of the Home Screen on iPhone that displays hint text for the Action button. The hint text is Hold for Silent.](https://docs-assets.developer.apple.com/published/57dfc914de079eeade28d459822295e0/controls-action-button-coaching-text-on~dark%402x.png)
![A partial screenshot of the Home Screen on iPhone that displays hint text for the Action button. The hint text is Hold for Ring.](https://docs-assets.developer.apple.com/published/09b3a4a0d3b05cee9a9eb007863306da/controls-action-button-coaching-text-off~dark%402x.png)
**If your control title or value can vary, include a placeholder.** Placeholder information tells people what your control does when the title and value are situational. The system displays this information when someone brings up the controls gallery in Control Center or the Lock Screen and chooses your control, or before they assign it to the Action button.
**Hide sensitive information when the device is locked.** When the device is locked, consider having the system redact the title and value to hide personal or security-related information. Specify if the system needs to redact the symbol state as well. If specified, the system redacts the title and value, and displays the symbol in its off state.
![A medium-size control toggle displaying a symbol of a light bulb, a title, and value text.](https://docs-assets.developer.apple.com/published/b38ee0c8c24dfea394e29ebd88bddbb9/control-regular-text~dark%402x.png)
![A medium-size control toggle with redacted text.](https://docs-assets.developer.apple.com/published/01249be2a2aa2af44d8587e990c21ada/control-redacted-text~dark%402x.png)
**Require authentication for actions that affect security.** For example, require people to unlock their device to access controls to lock or unlock the door to their house or start their car. For developer guidance, see [IntentAuthenticationPolicy](../AppIntents/IntentAuthenticationPolicy.md).

## Camera experiences on a locked device
If your app supports camera capture, starting with iOS 18 you can create a control that launches directly to your app’s camera experience while the device is locked. For any task beyond capture, a person must authenticate and unlock their device to complete the task in your app. For developer guidance, see [LockedCameraCapture](../LockedCameraCapture.md).
**Use the same camera UI in your app and your camera experience.** Sharing UI leverages people’s familiarity with the app. By using the same UI, the transition to the app is seamless when someone captures content and taps a button to perform additional tasks, such as posting to a social network or editing a photo.
**Provide instructions for adding the control.** Help people understand how to add the control that launches this camera experience.

## Platform considerations
*No additional considerations for iOS, iPadOS, or macOS. Not supported in watchOS, tvOS, or visionOS.*

## Resources

#### Related
[Widgets](widgets.md)
[Action button](action-button.md)

#### Developer documentation
[LockedCameraCapture](../LockedCameraCapture.md)
[WidgetKit](../WidgetKit.md)

## Change log
| Date | Changes |
| --- | --- |
| June 10, 2024 | New page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/controls](https://developer.apple.com/design/human-interface-guidelines/controls)*
