# NSApplication.ActivationPolicy.accessory

**Framework**: AppKit  
**Kind**: case

The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.

**Availability**:
- macOS ?+

## Declaration

```swift
case accessory
```

#### Discussion

This corresponds to value of the `LSUIElement` key in the application’s `Info.plist` being `1`.

## See Also

- [NSApplication.ActivationPolicy.regular](nsapplication/activationpolicy-swift.enum/regular.md)
  The application is an ordinary app that appears in the Dock and may have a user interface.
- [NSApplication.ActivationPolicy.prohibited](nsapplication/activationpolicy-swift.enum/prohibited.md)
  The application doesn’t appear in the Dock and may not create windows or be activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum/accessory)*