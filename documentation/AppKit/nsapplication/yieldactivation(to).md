# yieldActivation(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Explicitly allows another app to make itself active.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func yieldActivation(to application: NSRunningApplication)
```

```objc
- (void) yieldActivationToApplication:(NSRunningApplication *) application;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Discussion

Calling this method doesn’t deactivate the yielding app, nor does it activate the  app you yield to. For cooperative activation, the other app must request activation in the future by calling [`activate()`](./activate%28%29.md) or equivalent.

## Parameters

- `application`: The app to yield activation state to.

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
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](./yieldactivation%28toapplicationwithbundleidentifier%29.md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](./activationoptions.md)
  The following flags are for [`activate(options:)`](../nsrunningapplication/activate%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/yieldactivation(to:))*