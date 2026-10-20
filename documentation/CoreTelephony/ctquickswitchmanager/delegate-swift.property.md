# delegate

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

An object the system notifies to respond to quick switch events.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
weak var delegate: (any CTQuickSwitchManager.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CTQuickSwitchManagerDelegate> delegate;
```

## See Also

### Adopting iPhone quick switch
- [class CTQuickSwitchManager](../ctquickswitchmanager.md)
  An object that enables an app to register and query a device’s quick switch state.
- [CTQuickSwitchManager.Delegate](./delegate-swift.protocol.md)
  Methods you implement to respond to changes in a device’s quick switch state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/delegate-swift.property)*