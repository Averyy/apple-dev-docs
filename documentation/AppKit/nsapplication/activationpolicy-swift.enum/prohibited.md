# NSApplication.ActivationPolicy.prohibited

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The application doesn’t appear in the Dock and may not create windows or be activated.

**Availability**:
- macOS

## Declaration

```swift
case prohibited
```

```c
NSApplicationActivationPolicyProhibited
```

## Discussion

This corresponds to the value of the `LSBackgroundOnly` key in the application’s `Info.plist` file being `1`. This is also the default for unbundled executables that don’t have `Info.plist` files.

## See Also

### Activation Policies
- [NSApplication.ActivationPolicy.regular](./regular.md)
  The application is an ordinary app that appears in the Dock and may have a user interface.
- [NSApplication.ActivationPolicy.accessory](./accessory.md)
  The application doesn’t appear in the Dock and doesn’t have a menu bar, but it may be activated programmatically or by clicking on one of its windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activationpolicy-swift.enum/prohibited)*