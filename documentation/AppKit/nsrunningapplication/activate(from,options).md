# activate(from:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to activate the application using the specified options.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func activate(from application: NSRunningApplication, options: NSApplication.ActivationOptions = []) -> Bool
```

```objc
- (BOOL) activateFromApplication:(NSRunningApplication *) application options:(NSApplicationActivationOptions) options;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the request is allowed by the system, otherwise [`false`](../../Swift/false.md).

## Discussion

Use this method to request app activation. Calling this method doesn’t guarantee app activation. For cooperative activation, the other application should call [`yieldActivation(to:)`](../nsapplication/yieldactivation%28to%29.md) or equivalent prior to the target application invoking [`activate()`](../nsapplication/activate%28%29.md).

## Parameters

- `application`: The application to activate.
- `options`: The options to use during activation.

## See Also

### Activating applications
- [func activate(options: NSApplication.ActivationOptions) -> Bool](./activate%28options%29.md)
  Attempts to activate the application using the specified options.
- [var isActive: Bool](./isactive.md)
  Indicates whether the application is currently frontmost.
- [NSApplication.ActivationOptions](../nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](./activate%28options%29.md).
- [var activationPolicy: NSApplication.ActivationPolicy](./activationpolicy.md)
  Indicates the activation policy of the application.
- [NSApplication.ActivationPolicy](../nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](./activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/activate(from:options:))*