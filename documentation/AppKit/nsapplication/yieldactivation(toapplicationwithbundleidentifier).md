# yieldActivation(toApplicationWithBundleIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Explicitly allows another app to make itself active.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func yieldActivation(toApplicationWithBundleIdentifier bundleIdentifier: String)
```

```objc
- (void) yieldActivationToApplicationWithBundleIdentifier:(NSString *) bundleIdentifier;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Calling this method doesn’t deactivate the yielding app, nor does it activate the  app you yield to. For cooperative activation, the other app must request activation in the future by calling [`activate()`](./activate%28%29.md) or equivalent.

Use this method to yield activation to apps that aren’t running at the time the method invokes. If it’s known that the target application is running, use [`yieldActivation(to:)`](./yieldactivation%28to%29.md) instead.

## Parameters

- `bundleIdentifier`: The bundle identifier to yield activation state to.

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
- [NSApplication.ActivationOptions](./activationoptions.md)
  The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/yieldactivation(toapplicationwithbundleidentifier:))*