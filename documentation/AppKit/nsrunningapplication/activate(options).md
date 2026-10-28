# activate(options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to activate the application using the specified options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activate(options: NSApplication.ActivationOptions = []) -> Bool
```

```objc
- (BOOL) activateWithOptions:(NSApplicationActivationOptions) options;
```

## Return Value

[`true`](../../Swift/true.md) if the application was activated successfully, otherwise [`false`](../../Swift/false.md).

## Discussion

This method will return [`false`](../../Swift/false.md) if the application has quit, or is not a type of application than can be activated.

## Parameters

- `options`: The options to use when activating the application. See [`NSApplication.ActivationOptions`](../nsapplication/activationoptions.md) for the possible values.

## See Also

### Activating applications
- [func activate(from: NSRunningApplication, options: NSApplication.ActivationOptions) -> Bool](./activate%28from,options%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/activate(options:))*