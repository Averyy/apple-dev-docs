# Playing haptic feedback in your app

**Framework**: Apple Pencil

Provide tactile feedback when people perform certain actions in your app.

#### Overview

Haptic feedback provides a tactile response, such as a tap, that draws attention and reinforces both actions and events. While many system-provided interface elements (for example, pickers, switches, and sliders) automatically provide haptic feedback, you can add feedback to custom views and controls in your app when it’s suitable.

##### Use Feedback Intentionally

When providing feedback:

- Always use feedback for its intended purpose. Don’t select a haptic because of the way it feels.
- The source of the feedback must be clear to the user. For example, the feedback must match a visual change in the user interface, or must be in response to a user action. Feedback should never come as a surprise.
- Don’t overuse feedback. Overuse can cause confusion and diminish the feedback’s significance.

For design guidance, read Human Interface Guidelines > [`Playing haptics`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/playing-haptics).

##### Choose the Type of Feedback

SwiftUI and UIKit have different APIs for providing haptic feedback. Learn more about each style of haptic feedback and choose what makes sense for your app.

##### Associate the Feedback with a View

To play haptic feedback in your app, you need to add the feedback to a view.

##### Define When to Play Feedback

Haptic feedback occurs in response to something, like an action or event. You need to define what to trigger feedback in response to.

Using the feedback APIs in SwiftUI and UIKit doesn’t play haptics directly. Instead, it informs the system of the event. The system then determines whether to play the haptics based on the device, the app state, the amount of battery power remaining, and other factors.

For example, haptic feedback plays only:

- On a device with hardware for haptic feedback
- When the app is running in the foreground
- When the system Haptics setting is on

Not all types of haptic feedback play on every type of device. As a general rule, trust the system to determine whether it should play feedback. Don’t check the device type or app state to conditionally trigger feedback. After you decide how you want to use feedback, always trigger it when the appropriate events occur. The system ignores any requests that it can’t fulfill.

##### Play Feedback for Selection Events

Use selection feedback to communicate movement through a series of discrete values. For example, you might trigger selection feedback to indicate that a UI element’s values are changing.

##### Play Feedback for Canvas Events

Use canvas feedback to indicate when a drawing event occurs, such as an object snapping to a guide or ruler. When using Apple Pencil Pro with a compatible iPad, this type of feedback can provide a tactile response.

###### Related Reference in Swiftui

###### Related Reference in Uikit


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepencil/playing-haptic-feedback-in-your-app)*