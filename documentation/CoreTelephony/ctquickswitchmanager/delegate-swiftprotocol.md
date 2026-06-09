# CTQuickSwitchManager.Delegate

**Framework**: Core Telephony  
**Kind**: protocol

Methods you implement to respond to changes in a device’s quick switch state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

## Topics

### Responding to quick switch state changes
- [func quickSwitchManager(CTQuickSwitchManager, didChangeTo: CTQuickSwitchState)](ctquickswitchmanager/delegate-swift.protocol/quickswitchmanager(_:didchangeto:).md)
  Indicates there’s been a change in device’s quick switch state.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CTQuickSwitchManager](ctquickswitchmanager.md)
  An object that enables an app to register and query a device’s quick switch state.
- [var delegate: (any CTQuickSwitchManager.Delegate)?](ctquickswitchmanager/delegate-swift.property.md)
  An object the system notifies to respond to quick switch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/delegate-swift.protocol)*