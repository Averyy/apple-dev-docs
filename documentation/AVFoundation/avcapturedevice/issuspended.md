# isSuspended

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device is in a suspended state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var isSuspended: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSuspended) BOOL suspended;
```

#### Discussion

This property is key-value observable.

## See Also

### Accessing device state
- [var isConnected: Bool](./isconnected.md)
  A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [var isInUseByAnotherApplication: Bool](./isinusebyanotherapplication.md)
  A Boolean value that indicates whether another app is using the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/issuspended)*