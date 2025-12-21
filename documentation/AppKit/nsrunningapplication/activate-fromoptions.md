# activate(from:options:)

**Framework**: AppKit  
**Kind**: method

Attempts to activate the application using the specified options.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func activate(from application: NSRunningApplication, options: NSApplication.ActivationOptions = []) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the request is allowed by the system, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method to request app activation. Calling this method doesn’t guarantee app activation. For cooperative activation, the other application should call [`yieldActivation(to:)`](nsapplication/yieldactivation(to:).md) or equivalent prior to the target application invoking [`activate()`](nsapplication/activate().md).

## Parameters

- `application`: The application to activate.
- `options`: The options to use during activation.

## See Also

- [func activate(options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(options:).md)
  Attempts to activate the application using the specified options.
- [var isActive: Bool](nsrunningapplication/isactive.md)
  Indicates whether the application is currently frontmost.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).
- [var activationPolicy: NSApplication.ActivationPolicy](nsrunningapplication/activationpolicy.md)
  Indicates the activation policy of the application.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/activate(from:options:))*