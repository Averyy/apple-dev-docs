# isInUseByAnotherApplication

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether another app is using the device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
var isInUseByAnotherApplication: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isInUseByAnotherApplication) BOOL inUseByAnotherApplication;
```

#### Discussion

This property is key-value observable.

## See Also

### Accessing device state
- [var isConnected: Bool](./isconnected.md)
  A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [var isSuspended: Bool](./issuspended.md)
  A Boolean value that indicates whether the device is in a suspended state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isinusebyanotherapplication)*