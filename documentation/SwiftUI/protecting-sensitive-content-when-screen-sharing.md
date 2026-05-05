# Protecting sensitive content when screen sharing and remote control are active

**Framework**: SwiftUI

Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.

#### Overview

Screen sharing and remote control features offer people useful ways to collaborate. As screen sharing becomes more common, apps that handle sensitive data — such as banking, payments, and healthcare apps — should take steps to protect content during active capture sessions.

iOS and iPadOS provide a built-in API to detect when the system captures a scene. Respond to this signal and take proactive steps in your app to protect sensitive content during any capture session.

#### Detect When the System Captures Your Apps Content

When a screen capture session is active — including screen recording, mirroring, or remote control — the system updates the scene’s capture state. Use the [`isSceneCaptured`](EnvironmentValues/isSceneCaptured.md) environment value in SwiftUI or [`sceneCaptureState`](https://developer.apple.com/documentation/UIKit/UITraitCollection/sceneCaptureState) in UIKit to observe this state. When the state changes, update your UI accordingly — for example, replacing sensitive views with redacted or placeholder content.

**SwiftUI**:

```swift
struct AccountView: View {
    @Environment(\.isSceneCaptured) private var isSceneCaptured

    var body: some View {
        if isSceneCaptured {
            // Replace `RedactedContentView` with your redacted or placeholder view.
            RedactedContentView()
        } else {
            // Replace `SensitiveContentView` with your content view.
            SensitiveContentView()
        }
    }
}
```

**UIKit**:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // Register to observe scene capture state changes.
    registerForTraitChanges([UITraitSceneCaptureState.self]) { (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateContentVisibility()
    }
    // Apply the initial state on load.
    updateContentVisibility()
}

func updateContentVisibility() {
    let isCaptured = traitCollection.sceneCaptureState != .notCaptured
    // Replace `accountNumberLabel` and `balanceLabel` with the sensitive UI elements you want to hide.
    accountNumberLabel.isHidden = isCaptured
    balanceLabel.isHidden = isCaptured
}
```

> **Note**: `sceneCaptureState` doesn’t differentiate between capture types. Screen recording, AirPlay mirroring, and remote control all produce the same signal.

#### Respond to Capture Sessions

The right response depends on the sensitivity of the data your app handles and the potential impact to people if that content is exposed during a capture session. An app that displays financial account details or personal health information may warrant stronger protections than a general-purpose app. Assess the appropriate level of protection for people using your app to determine how to respond when your app detects a capture session:

- **Inform the person.** Display a banner or in-app notification letting people know their screen is being shared.
- **Hide or redact sensitive fields.** Replace account numbers, balances, card details, and passwords with placeholder text or a blur overlay. The Passwords app uses a similar pattern to protect sensitive content from screenshots.
- **Disable high-risk actions.** Prevent fund transfers, password reveals, or other irreversible operations from completing while capture is active.

#### Balance Protection with Usability

[`sceneCaptureState`](https://developer.apple.com/documentation/UIKit/UITraitCollection/sceneCaptureState) activates for all capture events, including everyday uses like recording a tutorial or mirroring to a personal Apple TV. Keep these considerations in mind when deciding how to respond:

- **Apply protections selectively.** Target the highest-risk areas of your app rather than blocking functionality broadly. A blanket app-level lockdown may frustrate people with legitimate screen-sharing needs.
- **Use neutral language.** Avoid messaging that implies the person is under attack. A calm, informative notification — such as “Screen sharing is active. Some content is protected during this session.” — is less alarming and more effective.
- **Weigh the tradeoff for your audience.** A banking app with stricter security requirements may justify more restrictive behavior than a general-purpose app. Design your response based on your app’s specific risk profile.

## See Also

- [Designing your app for the Always On state](../watchOS-Apps/designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [func privacySensitive(Bool) -> some View](view/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.
- [struct RedactionReasons](redactionreasons.md)
  The reasons to apply a redaction to data displayed on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/protecting-sensitive-content-when-screen-sharing)*