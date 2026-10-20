# NSApplication.ActivationPolicy

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Activation policies (used by [`activationPolicy`](../nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.

**Availability**:
- macOS

## Declaration

```swift
enum ActivationPolicy
```

```c
enum NSApplicationActivationPolicy : NSInteger;
```

## Topics

### Activation Policies
- [NSApplication.ActivationPolicy.regular](./activationpolicy-swift.enum/regular.md)
  The application is an ordinary app that appears in the Dock and may have a user interface.
- [NSApplication.ActivationPolicy.accessory](./activationpolicy-swift.enum/accessory.md)
  The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.
- [NSApplication.ActivationPolicy.prohibited](./activationpolicy-swift.enum/prohibited.md)
  The application doesn’t appear in the Dock and may not create windows or be activated.
### Initializers
- [init?(rawValue: Int)](./activationpolicy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the activation policy
- [func activationPolicy() -> NSApplication.ActivationPolicy](./activationpolicy%28%29.md)
  Returns the app’s activation policy.
- [func setActivationPolicy(NSApplication.ActivationPolicy) -> Bool](./setactivationpolicy%28_%29.md)
  Attempts to modify the app’s activation policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum)*