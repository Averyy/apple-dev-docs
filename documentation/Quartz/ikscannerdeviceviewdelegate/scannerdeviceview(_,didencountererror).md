# scannerDeviceView(_:didEncounterError:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Invoked whenever the scanner encounters an error.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func scannerDeviceView(_ scannerDeviceView: IKScannerDeviceView!, didEncounterError error: (any Error)!)
```

```objc
- (void) scannerDeviceView:(IKScannerDeviceView *) scannerDeviceView didEncounterError:(NSError *) error;
```

## Parameters

- `scannerDeviceView`: The scanner device that sent the message.
- `error`: The error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/scannerdeviceview(_:didencountererror:))*