# activate()

**Framework**: AppKit  
**Kind**: method

Activates the receiver app, if appropriate.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func activate()
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Use this method to request app activation; calling this method doesn’t guarantee app activation. For cooperative activation, the other app should call [`yieldActivation(to:)`](nsapplication/yieldactivation(to:).md) or equivalent before the target app invokes [`activate()`](nsapplication/activate().md).

Invoking [`activate()`](nsapplication/activate().md) on an already-active application cancels any pending activation yields by the receiver.

## See Also

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activate())*