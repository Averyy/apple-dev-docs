# NSApplication.ActivationPolicy.regular

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The application is an ordinary app that appears in the Dock and may have a user interface.

**Availability**:
- macOS

## Declaration

```swift
case regular
```

```c
NSApplicationActivationPolicyRegular
```

## Discussion

This policy is the default for bundled apps, unless overridden in the `Info.plist`.

## See Also

### Activation Policies
- [NSApplication.ActivationPolicy.accessory](./accessory.md)
  The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.
- [NSApplication.ActivationPolicy.prohibited](./prohibited.md)
  The application doesn’t appear in the Dock and may not create windows or be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum/regular)*