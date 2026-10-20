# activationPolicy

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the activation policy of the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var activationPolicy: NSApplication.ActivationPolicy { get }
```

```objc
@property (readonly) NSApplicationActivationPolicy activationPolicy;
```

#### Discussion

The value returned by this property is usually fixed, but it may change through a call to [`activate(options:)`](./activate%28options%29.md).

This property is observable using key-value observing.

## See Also

### Activating applications
- [func activate(options: NSApplication.ActivationOptions) -> Bool](./activate%28options%29.md)
  Attempts to activate the application using the specified options.
- [func activate(from: NSRunningApplication, options: NSApplication.ActivationOptions) -> Bool](./activate%28from,options%29.md)
  Attempts to activate the application using the specified options.
- [var isActive: Bool](./isactive.md)
  Indicates whether the application is currently frontmost.
- [NSApplication.ActivationOptions](../nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](./activate%28options%29.md).
- [NSApplication.ActivationPolicy](../nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](./activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/activationpolicy)*