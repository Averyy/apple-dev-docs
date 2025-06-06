# setActivationPolicy(_:)

**Framework**: AppKit  
**Kind**: method

Attempts to modify the app’s activation policy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func setActivationPolicy(_ activationPolicy: NSApplication.ActivationPolicy) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the policy switch succeded; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You can set any activation policy in macOS 10.9 and later; in macOS 10.8 and earlier, you can only set the activation policy to  `NSApplicationActivationPolicyProhibited` or `NSApplicationActivationPolicyRegular`.

## Parameters

- `activationPolicy`: The desired activation policy.

## See Also

- [func activationPolicy() -> NSApplication.ActivationPolicy](nsapplication/activationpolicy.md)
  Returns the app’s activation policy.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/setactivationpolicy(_:))*