# externalSyncDevice(_:failedWithError:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
optional func externalSyncDevice(_ device: AVExternalSyncDevice, failedWithError error: (any Error)?)
```

```objc
- (void) externalSyncDevice:(AVExternalSyncDevice *) device failedWithError:(NSError *) error;
```

## See Also

### Responding to device events
- [func externalSyncDeviceStatusDidChange(AVExternalSyncDevice)](./externalsyncdevicestatusdidchange%28_%29.md)
  Informs your delegate when the external sync device status has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicedelegate/externalsyncdevice(_:failedwitherror:))*