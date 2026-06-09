# delegate

**Framework**: Core Telephony  
**Kind**: property

An object the system notifies to respond to quick switch events.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
weak var delegate: (any CTQuickSwitchManager.Delegate)? { get set }
```

## See Also

- [class CTQuickSwitchManager](ctquickswitchmanager.md)
  An object that enables an app to register and query a device’s quick switch state.
- [CTQuickSwitchManager.Delegate](ctquickswitchmanager/delegate-swift.protocol.md)
  Methods you implement to respond to changes in a device’s quick switch state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/delegate-swift.property)*