# IOUSBHostCompletionHandler

**Framework**: IOUSBHost  
**Kind**: typealias

The completion handler for asynchronous control, bulk, and interrupt transfers.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostCompletionHandler = (IOReturn, Int) -> Void
```

## Parameters

- `status`: The result for the transfer.
- `bytesTransferred`: The number of bytes the request transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcompletionhandler)*