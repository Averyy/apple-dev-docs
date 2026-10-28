# scannerDevice:didScanToURL:data:

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the scanner device receives the requested scan.

**Availability**:
- macOS 10.6+ - Deprecated in 10.7

## Declaration

```objc
- (void) scannerDevice:(ICScannerDevice *) scanner didScanToURL:(NSURL *) url data:(NSData *) data;
```

## Discussion

If the [`selectedFunctionalUnit`](../icscannerdevice/selectedfunctionalunit.md) is a document feeder, then this message is sent once for each scanned page.

This method has been deprecated. Use [`scannerDevice(_:didScanTo:)`](./scannerdevice%28_,didscanto%29-10whl.md) for file-based transfer, or [`scannerDevice(_:didScanTo:)`](./scannerdevice%28_,didscanto%29-6tht3.md) for memory-based transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice:didscantourl:data:)*