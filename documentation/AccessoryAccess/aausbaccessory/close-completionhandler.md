# close(completionHandler:)

**Framework**: Accessory Access  
**Kind**: method

Closes all connections to the USB accessory for this process.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func close() async throws
```

#### Discussion

> ⚠️ **Warning**: Closing an accessory by calling the `destroy()` method on an [`IOUSBHostDevice`](https://developer.apple.com/documentation/IOUSBHost/IOUSBHostDevice) is a blocking operation. Such an operation causes a deadlock, if you call it from a completion handler.

This operation closes the USB accessory, that the app previously opened through [`open(serviceQueue:completionHandler:)`](aausbaccessory/open(servicequeue:completionhandler:).md). Once this operation completes, the framework invalidates any [`IOUSBHostDevice`](https://developer.apple.com/documentation/IOUSBHost/IOUSBHostDevice) object it previously returned and you can’t use it for USB transfers. This operation has the same effect as calling the destroy method on [`IOUSBHostDevice`](https://developer.apple.com/documentation/IOUSBHost/IOUSBHostDevice).

Once the app closes the accessory, the app can re-open the accessory using this process or any other worker process of this client application for exclusive access using [`open(serviceQueue:completionHandler:)`](aausbaccessory/open(servicequeue:completionhandler:).md).

## Parameters

- `completionHandler`: A block the framework calls after the client has successfully closed the USB accessory. The error parameter the framework passes to the block is `nil` if the operation was successful. The framework invokes the block on an arbitrary thread.

## See Also

- [func open(serviceQueue: dispatch_queue_t?, completionHandler: (IOUSBHostDevice, (any Error)?) -> Void)](aausbaccessory/open(servicequeue:completionhandler:).md)
  Opens a connection to the USB accessory for this process to access it exclusively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/close(completionhandler:))*