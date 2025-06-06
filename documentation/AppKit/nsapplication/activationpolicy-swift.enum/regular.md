# NSApplication.ActivationPolicy.regular

**Framework**: AppKit  
**Kind**: case

The application is an ordinary app that appears in the Dock and may have a user interface.

**Availability**:
- macOS ?+

## Declaration

```swift
case regular
```

#### Discussion

This policy is the default for bundled apps, unless overridden in the `Info.plist`.

## See Also

- [NSApplication.ActivationPolicy.accessory](nsapplication/activationpolicy-swift.enum/accessory.md)
  The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.
- [NSApplication.ActivationPolicy.prohibited](nsapplication/activationpolicy-swift.enum/prohibited.md)
  The application doesn’t appear in the Dock and may not create windows or be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum/regular)*