# Passing control from one app to another with cooperative activation

**Framework**: Appkit

Request focus for your app, and coordinate passing control from one app to another.

#### Overview

When someone uses your app and another app unexpectedly steals focus, the user experience can be compromised. Not only is it inconvenient for people to switch back to their original app, if they’re typing when the switch occurs, they might accidentally enter text into the wrong app, inadvertently disclosing sensitive information.

Cooperative activation addresses this problem by making app activation a request instead of a command. Instead of apps stealing focus, they now request focus from the system when they’re ready. This means apps should set expectations accordingly when requesting activation and not assume the system will grant them activation. The system dynamically determines whether to grant activation state based on the context. This lets you request focus for your app when needed, and hand off focus from one app to another.

> **Note**:  Session 10054: [`What’s new in AppKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10054)

##### Request Activation to Gain Focus

When your app needs focus, call [`activate()`](nsapplication/activate().md) on your app’s [`shared`](nsapplication/shared.md) instance, or its shorthand version `NSApp`:

Calling this function sends a message to the system requesting activation for the app. Requesting activation doesn’t guarantee your app gains focus. People ultimately decide which apps gain focus by activating them through their device’s user interface. But if, after considering the user’s intent and larger system context, the system honors your app’s request, your app activates.

##### Transfer Control From One App to Another By Yielding and Then Activating

Passing control from one app to another is a two-step process.

1. First yield from the currently running active app to the target app that you want to gain focus.
2. Then activate the target app when it’s ready.

![A block diagram showing two app instances on the left stacked on top of one another, with arrows pointing out of the boxes into another box titled System makes a decision on the right. Within the topmost app instance box, titled Active app, is another box titled Yield to target. It’s sequentially to the left of a similar box in the bottom app instance titled Activate. The sequence of boxes implies you call Yield to target on the Active app instance before Activate on the Target app instance.](https://docs-assets.developer.apple.com/published/290772882a3166f50918eed2c57cf0dd/media-4311539%402x.png)

Only the active app can influence the activation context. It does so by yielding to an explicit target app before the target app activates. Then, when the target app requests activation, the system uses the yield as part of the context when making its decision. If the system honors the request, the active app deactivates, and the target app activates. Otherwise, the active app remains active. [`NSWorkspace`](nsworkspace.md) automatically handles this for you when opening URLs or applications.

For example, to pass control from your active app to another target app (such as TextEdit, which is a good test candidate because it comes installed on every Mac):

1. Get an instance of the target app you want to pass control to by calling [`runningApplications(withBundleIdentifier:)`](nsrunningapplication/runningapplications(withbundleidentifier:).md), passing in the bundle identifier of the target app.
2. Yield to the target app by calling [`yieldActivation(to:)`](nsapplication/yieldactivation(to:).md), passing the target app instance.
3. Then activate the target by calling [`activate()`](nsapplication/activate().md) on the target app instance.

Alternatively, if the app you want to pass control to isn’t currently running, call [`yieldActivation(toApplicationWithBundleIdentifier:)`](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md) on the `NSApp` instance, passing in the bundle identifier of the target app you want to activate.

Then call [`activate()`](nsapplication/activate().md) on the target app when it’s ready to gain focus.

Choosing between [`NSRunningApplication`](nsrunningapplication.md) or [`NSApplication`](nsapplication.md) for activation depends on which app you want to initiate the activation. Use `NSRunningApplication` if you want the active app to control when the target app activates. Use `NSApplication` (or `NSApp`) if you want the target app to activate itself.

##### Replace Calls to Deactivate

When you call [`yieldActivation(to:)`](nsapplication/yieldactivation(to:).md), there’s no need to call [`deactivate()`](nsapplication/deactivate().md) on the app losing focus. Cooperative activation APIs cause the receiver to draw inactive when another app activates. This is typically the behavior you want.

Replace calls to [`deactivate()`](nsapplication/deactivate().md) with [`yieldActivation(to:)`](nsapplication/yieldactivation(to:).md) or equivalent. There’s also no need to call `deactivate()` if an app is hidden by calling [`hide()`](nsrunningapplication/hide().md). The system implies deactivation when the app hides.

## See Also

- [func activate()](nsapplication/activate.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](nsapplication/deactivate.md)
  Deactivates the receiver.
- [var isActive: Bool](nsapplication/isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](nsapplication/yieldactivation(to:).md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/passing-control-from-one-app-to-another-with-cooperative-activation)*