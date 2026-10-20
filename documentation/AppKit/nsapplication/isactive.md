# isActive

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this is the active app.

**Availability**:
- macOS

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (readonly, getter=isActive) BOOL active;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the app is active or [`false`](../../Swift/false.md) if it’s not.

## See Also

### Related Documentation
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
### Activating and deactivating the app
- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](./activate%28%29.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the receiver.
- [func yieldActivation(to: NSRunningApplication)](./yieldactivation%28to%29.md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](./yieldactivation%28toapplicationwithbundleidentifier%29.md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](./activationoptions.md)
  The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isactive)*