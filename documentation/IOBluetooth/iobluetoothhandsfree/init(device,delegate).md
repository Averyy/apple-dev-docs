# init(device:delegate:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Create a new IOBluetoothHandsFree object

**Availability**:
- macOS 10.7+

## Declaration

```swift
init!(device: IOBluetoothDevice!, delegate inDelegate: (any IOBluetoothHandsFreeDelegate)!)
```

```objc
- (instancetype) initWithDevice:(IOBluetoothDevice *) device delegate:(id<IOBluetoothHandsFreeDelegate>) inDelegate;
```

#### Return Value

A newly created IOBluetoothHandsFreeAudioGateway object on success, nil on failure

#### Discussion

This method should be called on a subclass (IOBluetoothHandsFreeDevice or IOBluetoothHandsFreeAudioGateway) to get full functionality.

## Parameters

- `device`: An IOBluetoothDevice
- `inDelegate`: An object to act as delegate that implements the IOBluetoothHandsFreeDelegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/init(device:delegate:))*