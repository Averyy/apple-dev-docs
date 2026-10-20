# sendIORequest(with:transactionList:transactionListCount:firstFrameNumber:options:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 12.0+

## Declaration

```swift
func sendIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) throws
```

```objc
- (BOOL) sendIORequestWithData:(NSMutableData *) data transactionList:(IOUSBHostIsochronousTransaction *) transactionList transactionListCount:(NSUInteger) transactionListCount firstFrameNumber:(uint64_t) firstFrameNumber options:(IOUSBHostIsochronousTransferOptions) options error:(NSError **) error;
```

## See Also

### Instance Methods
- [func enqueueIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions, completionHandler: ((IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void)?) throws](./enqueueiorequest%28with,transactionlist,transactionlistcount,firstframenumber,options,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/sendiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:))*