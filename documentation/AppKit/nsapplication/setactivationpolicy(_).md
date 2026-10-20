# setActivationPolicy(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to modify the app’s activation policy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setActivationPolicy(_ activationPolicy: NSApplication.ActivationPolicy) -> Bool
```

```objc
- (BOOL) setActivationPolicy:(NSApplicationActivationPolicy) activationPolicy;
```

#### Return Value

[`true`](../../Swift/true.md) if the policy switch succeded; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You can set any activation policy in macOS 10.9 and later; in macOS 10.8 and earlier, you can only set the activation policy to  `NSApplicationActivationPolicyProhibited` or `NSApplicationActivationPolicyRegular`.

## Parameters

- `activationPolicy`: The desired activation policy.

## See Also

### Configuring the activation policy
- [func activationPolicy() -> NSApplication.ActivationPolicy](./activationpolicy%28%29.md)
  Returns the app’s activation policy.
- [NSApplication.ActivationPolicy](./activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](../nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/setactivationpolicy(_:))*