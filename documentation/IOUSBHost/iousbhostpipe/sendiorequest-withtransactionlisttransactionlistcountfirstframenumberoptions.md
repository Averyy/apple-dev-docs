# sendIORequest(with:transactionList:transactionListCount:firstFrameNumber:options:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 12.0+

## Declaration

```swift
func sendIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) throws
```

## See Also

- [func enqueueIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void)?) throws](iousbhostpipe/enqueueiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:))*