# powerState

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Gets the controller power state

**Availability**:
- macOS

## Declaration

```swift
var powerState: BluetoothHCIPowerState { get }
```

```objc
@property (readonly) BluetoothHCIPowerState powerState;
```

## Return Value

The current controller’s power state. This will be 1 for on, or 0 for off. Only Apple Bluetooth adapters support power off


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller/powerstate)*