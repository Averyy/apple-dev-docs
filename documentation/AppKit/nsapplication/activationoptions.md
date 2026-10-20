# NSApplication.ActivationOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).

**Availability**:
- macOS

## Declaration

```swift
struct ActivationOptions
```

```c
enum NSApplicationActivationOptions : NSUInteger;
```

## Topics

### Options
- [static var activateAllWindows: NSApplication.ActivationOptions](./activationoptions/activateallwindows.md)
  By default, activation brings only the main and key windows forward.  If you specify NSApplicationActivateAllWindows, all of the application’s windows are brought forward.
- [static var activateIgnoringOtherApps: NSApplication.ActivationOptions](./activationoptions/activateignoringotherapps.md)
  The application is activated regardless of the currently active app.
### Initializers
- [init(rawValue: UInt)](./activationoptions/init%28rawvalue%29.md)
  Initializes a new activation options structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Activating and deactivating the app
- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](./activate%28%29.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the receiver.
- [var isActive: Bool](./isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](./yieldactivation%28to%29.md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](./yieldactivation%28toapplicationwithbundleidentifier%29.md)
  Explicitly allows another app to make itself active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationoptions)*