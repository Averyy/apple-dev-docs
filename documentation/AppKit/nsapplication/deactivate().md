# deactivate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deactivates the receiver.

**Availability**:
- macOS

## Declaration

```swift
func deactivate()
```

```objc
- (void) deactivate;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

## Discussion

Normally, you shouldn’t invoke this method—AppKit is responsible for proper deactivation.

## See Also

### Related Documentation
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
### Activating and deactivating the app
- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](./activate%28%29.md)
  Activates the receiver app, if appropriate.
- [var isActive: Bool](./isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](./yieldactivation%28to%29.md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](./yieldactivation%28toapplicationwithbundleidentifier%29.md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](./activationoptions.md)
  The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/deactivate())*