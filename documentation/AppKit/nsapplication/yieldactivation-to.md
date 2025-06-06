# yieldActivation(to:)

**Framework**: AppKit  
**Kind**: method

Explicitly allows another app to make itself active.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func yieldActivation(to application: NSRunningApplication)
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Calling this method doesn’t deactivate the yielding app, nor does it activate the  app you yield to. For cooperative activation, the other app must request activation in the future by calling [`activate()`](nsapplication/activate().md) or equivalent.

## Parameters

- `application`: The app to yield activation state to.

## See Also

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](nsapplication/activate.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](nsapplication/deactivate.md)
  Deactivates the receiver.
- [var isActive: Bool](nsapplication/isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/yieldactivation(to:))*