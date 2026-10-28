# getLastServicesUpdate()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the date/time of the last SDP query.

**Availability**:
- macOS

## Declaration

```swift
func getLastServicesUpdate() -> Date!
```

```objc
- (NSDate *) getLastServicesUpdate;
```

## Return Value

Returns the date/time of the last SDP query. If an SDP query has never been performed on the device, nil is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/getlastservicesupdate())*