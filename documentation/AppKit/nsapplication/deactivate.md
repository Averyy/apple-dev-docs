# deactivate()

**Framework**: AppKit  
**Kind**: method

Deactivates the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deactivate()
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Normally, you shouldn’t invoke this method—AppKit is responsible for proper deactivation.

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](nsapplication/activate.md)
  Activates the receiver app, if appropriate.
- [var isActive: Bool](nsapplication/isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](nsapplication/yieldactivation(to:).md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/deactivate())*