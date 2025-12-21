# isActive

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether this is the active app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isActive: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the app is active or [`false`](https://developer.apple.com/documentation/Swift/false) if it’s not.

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](nsapplication/activate.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](nsapplication/deactivate.md)
  Deactivates the receiver.
- [func yieldActivation(to: NSRunningApplication)](nsapplication/yieldactivation(to:).md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isactive)*