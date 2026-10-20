# connectSCO()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Open a SCO connection with the device

**Availability**:
- macOS 10.7+

## Declaration

```swift
func connectSCO()
```

```objc
- (void) connectSCO;
```

#### Discussion

Opens a SCO connection with the device. The device must already have a service level connection or this will return immediately. Delegate methods will be called once the connection is complete of a failure occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/connectsco())*