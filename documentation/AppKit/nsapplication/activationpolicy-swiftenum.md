# NSApplication.ActivationPolicy

**Framework**: AppKit  
**Kind**: enum

Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.

**Availability**:
- macOS ?+

## Declaration

```swift
enum ActivationPolicy
```

## Topics

### Activation Policies
- [NSApplication.ActivationPolicy.regular](nsapplication/activationpolicy-swift.enum/regular.md)
  The application is an ordinary app that appears in the Dock and may have a user interface.
- [NSApplication.ActivationPolicy.accessory](nsapplication/activationpolicy-swift.enum/accessory.md)
  The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.
- [NSApplication.ActivationPolicy.prohibited](nsapplication/activationpolicy-swift.enum/prohibited.md)
  The application doesn’t appear in the Dock and may not create windows or be activated.
### Initializers
- [init?(rawValue: Int)](nsapplication/activationpolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func activationPolicy() -> NSApplication.ActivationPolicy](nsapplication/activationpolicy.md)
  Returns the app’s activation policy.
- [func setActivationPolicy(NSApplication.ActivationPolicy) -> Bool](nsapplication/setactivationpolicy(_:).md)
  Attempts to modify the app’s activation policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum)*