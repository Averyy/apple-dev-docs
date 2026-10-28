# activationPolicy()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the app’s activation policy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activationPolicy() -> NSApplication.ActivationPolicy
```

```objc
- (NSApplicationActivationPolicy) activationPolicy;
```

## Return Value

The app’s current activation policy.

## See Also

### Configuring the activation policy
- [func setActivationPolicy(NSApplication.ActivationPolicy) -> Bool](./setactivationpolicy%28_%29.md)
  Attempts to modify the app’s activation policy.
- [NSApplication.ActivationPolicy](./activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](../nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy())*