# quickSwitchManager(_:didChangeTo:)

**Framework**: Core Telephony  
**Kind**: method

Indicates there’s been a change in device’s quick switch state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
optional func quickSwitchManager(_ quickSwitchManager: CTQuickSwitchManager, didChangeTo state: CTQuickSwitchState)
```

#### Discussion

Implement this method to receive notification when the device’s quick switch state changes.

## See Also

- [enum CTQuickSwitchState](ctquickswitchstate.md)
  Values that describe a device’s quick switch status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/delegate-swift.protocol/quickswitchmanager(_:didchangeto:))*