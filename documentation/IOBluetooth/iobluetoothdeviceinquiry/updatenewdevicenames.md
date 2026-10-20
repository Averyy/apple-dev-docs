# updateNewDeviceNames

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Sets whether or not the inquiry object will retrieve the names of devices found during the search.

**Availability**:
- macOS

## Declaration

```swift
var updateNewDeviceNames: Bool { get set }
```

```objc
@property (assign) BOOL updateNewDeviceNames;
```

#### Discussion

The default value for the inquiry object is TRUE, unless this method is used to change it.

## Parameters

- `inValue`: Pass TRUE if names are to be updated, otherwise pass FALSE.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/updatenewdevicenames)*