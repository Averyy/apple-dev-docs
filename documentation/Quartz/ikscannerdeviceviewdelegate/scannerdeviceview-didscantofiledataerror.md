# scannerDeviceView(_:didScanTo:fileData:error:)

**Framework**: Quartz  
**Kind**: method

Invoked when the scan has completed and the data is available.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func scannerDeviceView(_ scannerDeviceView: IKScannerDeviceView!, didScanTo url: URL!, fileData data: Data!, error: (any Error)!)
```

#### Discussion

This method is called when the scan has completed..

If the `scannerDeviceView` [`transferMode`](ikscannerdeviceview/transfermode.md) is [`IKScannerDeviceViewTransferMode.fileBased`](ikscannerdeviceviewtransfermode/filebased.md), the scan will have been saved at the specified `url`. The URL will be in the download directory and be a complete path, including a ‘sequence number’ if the file already exists.

If the `scannerDeviceView` [`transferMode`](ikscannerdeviceview/transfermode.md) is [`IKScannerDeviceViewTransferMode.memoryBased`](ikscannerdeviceviewtransfermode/memorybased.md), the scanned data is contained in the data parameter. You can then take the action appropriate to your application.

In case of an error, the parameters (`url` and `data`) will be `NULL` and `error` (which may come directly from the scanner module / or the ImageCaptureCore framework) will describe why the scan or save failed.

## Parameters

- `scannerDeviceView`: The scanner device that sent the message.
- `url`: The URL to save the data.
- `data`: The data from the scan.
- `error`: Any error encountered during the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/scannerdeviceview(_:didscanto:filedata:error:))*