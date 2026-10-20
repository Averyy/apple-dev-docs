# scannerDeviceView(_:didScanTo:scanInfo:error:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func scannerDeviceView(_ scannerDeviceView: IKScannerDeviceView!, didScanTo data: ICScannerBandData!, scanInfo: [AnyHashable : Any]!, error: (any Error)!)
```

```objc
- (void) scannerDeviceView:(IKScannerDeviceView *) scannerDeviceView didScanToBandData:(ICScannerBandData *) data scanInfo:(NSDictionary *) scanInfo error:(NSError *) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/scannerdeviceview(_:didscanto:scaninfo:error:))*