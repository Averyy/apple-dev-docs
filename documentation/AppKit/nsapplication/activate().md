# activate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Activates the receiver app, if appropriate.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func activate()
```

```objc
- (void) activate;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Use this method to request app activation; calling this method doesn’t guarantee app activation. For cooperative activation, the other app should call [`yieldActivation(to:)`](./yieldactivation%28to%29.md) or equivalent before the target app invokes [`activate()`](./activate%28%29.md).

Invoking [`activate()`](./activate%28%29.md) on an already-active application cancels any pending activation yields by the receiver.

## See Also

### Activating and deactivating the app
- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the receiver.
- [var isActive: Bool](./isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](./yieldactivation%28to%29.md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](./yieldactivation%28toapplicationwithbundleidentifier%29.md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](./activationoptions.md)
  The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activate())*