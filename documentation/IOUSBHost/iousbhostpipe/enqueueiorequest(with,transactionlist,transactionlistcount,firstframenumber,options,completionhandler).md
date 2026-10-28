# enqueueIORequest(with:transactionList:transactionListCount:firstFrameNumber:options:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 14.0+
- macOS 12.0+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = [], completionHandler: (@Sendable (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void)? = nil) throws
```

```swift
func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>)
```

```objc
- (BOOL) enqueueIORequestWithData:(NSMutableData *) data transactionList:(IOUSBHostIsochronousTransaction *) transactionList transactionListCount:(NSUInteger) transactionListCount firstFrameNumber:(uint64_t) firstFrameNumber options:(IOUSBHostIsochronousTransferOptions) options error:(NSError **) error completionHandler:(IOUSBHostIsochronousTransactionCompletionHandler) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func sendIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions) throws](./sendiorequest%28with,transactionlist,transactionlistcount,firstframenumber,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:completionhandler:))*