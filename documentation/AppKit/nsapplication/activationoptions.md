# NSApplication.ActivationOptions

**Framework**: AppKit  
**Kind**: struct

The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
struct ActivationOptions
```

## Topics

### Options
- [static var activateAllWindows: NSApplication.ActivationOptions](nsapplication/activationoptions/activateallwindows.md)
  By default, activation brings only the main and key windows forward.  If you specify NSApplicationActivateAllWindows, all of the application’s windows are brought forward.
### Initializers
- [init(rawValue: UInt)](nsapplication/activationoptions/init(rawvalue:).md)
  Initializes a new activation options structure.
### Deprecated
- [static var activateIgnoringOtherApps: NSApplication.ActivationOptions](nsapplication/activationoptions/activateignoringotherapps.md)
  The application is activated regardless of the currently active app.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationoptions)*