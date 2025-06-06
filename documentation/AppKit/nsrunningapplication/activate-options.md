# activate(options:)

**Framework**: AppKit  
**Kind**: method

Attempts to activate the application using the specified options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activate(options: NSApplication.ActivationOptions = []) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the application was activated successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method will return [`false`](https://developer.apple.com/documentation/swift/false) if the application has quit, or is not a type of application than can be activated.

## Parameters

- `options`: The options to use when activating the application. See   for the possible values.

## See Also

- [func activate(from: NSRunningApplication, options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(from:options:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/activate(options:))*