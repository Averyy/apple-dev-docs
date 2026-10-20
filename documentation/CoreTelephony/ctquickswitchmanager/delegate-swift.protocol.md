# CTQuickSwitchManager.Delegate

**Framework**: Core Telephony  
**Kind**: protocol  
**Role**: Protocol

Methods you implement to respond to changes in a device’s quick switch state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

```objc
@protocol CTQuickSwitchManagerDelegate <NSObject>
```

## Topics

### Responding to quick switch state changes
- [func quickSwitchManager(CTQuickSwitchManager, didChangeTo: CTQuickSwitchState)](./delegate-swift.protocol/quickswitchmanager%28_,didchangeto%29.md)
  Indicates there’s been a change in device’s quick switch state.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Adopting iPhone quick switch
- [class CTQuickSwitchManager](../ctquickswitchmanager.md)
  An object that enables an app to register and query a device’s quick switch state.
- [var delegate: (any CTQuickSwitchManager.Delegate)?](./delegate-swift.property.md)
  An object the system notifies to respond to quick switch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/delegate-swift.protocol)*