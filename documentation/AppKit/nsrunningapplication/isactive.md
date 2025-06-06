# isActive

**Framework**: AppKit  
**Kind**: property

Indicates whether the application is currently frontmost.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

This property is observable using key-value observing.

## See Also

- [func activate(options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(options:).md)
  Attempts to activate the application using the specified options.
- [func activate(from: NSRunningApplication, options: NSApplication.ActivationOptions) -> Bool](nsrunningapplication/activate(from:options:).md)
  Attempts to activate the application using the specified options.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).
- [var activationPolicy: NSApplication.ActivationPolicy](nsrunningapplication/activationpolicy.md)
  Indicates the activation policy of the application.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/isactive)*