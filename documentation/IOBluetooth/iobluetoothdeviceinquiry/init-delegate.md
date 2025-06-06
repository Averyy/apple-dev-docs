# init(delegate:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes an alloc’d inquiry object, and sets the delegate object, as if -setDelegate: were called on it.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(delegate: Any!)
```

#### Return Value

A pointer to the initialized IOBluetoothDeviceInquiry object.

## Parameters

- `delegate`: A delegate object that wishes to receive messages from the inquiry object. Delegate methods are listed below, under IOBluetoothDeviceInquiryDelegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/init(delegate:))*