# activationPolicy()

**Framework**: AppKit  
**Kind**: method

Returns the app’s activation policy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func activationPolicy() -> NSApplication.ActivationPolicy
```

#### Return Value

The app’s current activation policy.

## See Also

- [func setActivationPolicy(NSApplication.ActivationPolicy) -> Bool](nsapplication/setactivationpolicy(_:).md)
  Attempts to modify the app’s activation policy.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy())*