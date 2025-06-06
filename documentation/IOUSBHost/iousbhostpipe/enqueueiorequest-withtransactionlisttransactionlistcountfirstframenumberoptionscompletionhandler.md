# enqueueIORequest(with:transactionList:transactionListCount:firstFrameNumber:options:completionHandler:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 12.0+

## Declaration

```swift
func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>)
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func enqueueIORequest(with data: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions = []) async throws -> (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>)
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func sendIORequest(with: NSMutableData, transactionList: UnsafeMutablePointer<IOUSBHostIsochronousTransaction>, transactionListCount: Int, firstFrameNumber: UInt64, options: IOUSBHostIsochronousTransferOptions) throws](iousbhostpipe/sendiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostpipe/enqueueiorequest(with:transactionlist:transactionlistcount:firstframenumber:options:completionhandler:))*