# open(serviceQueue:completionHandler:)

**Framework**: Accessory Access  
**Kind**: method  
**Role**: Instance Method

Opens a connection to the USB accessory for this process to access it exclusively.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func open(serviceQueue: dispatch_queue_t?, completionHandler: @escaping @Sendable (IOUSBHostDevice, (any Error)?) -> Void)
```

```swift
func open(serviceQueue: dispatch_queue_t?) async throws -> IOUSBHostDevice
```

```objc
- (void) openWithServiceQueue:(dispatch_queue_t) serviceQueue completionHandler:(void (^)(IOUSBHostDevice *_Nullable_on_error, NSError *)) completionHandler;
```

#### Discussion

This operation opens a connection to the USB accessory for exclusive access and returns its [`IOUSBHostDevice`](../../IOUSBHost/iousbhostdevice.md) object. An app can call this multiple times, subsequent calls will return the same `IOUSBHostDevice` instance.

When the process no longer needs exclusive access to this accessory, call [`close(completionHandler:)`](./close%28completionhandler%29.md) to close the accessory. This will close all open connections to the accessory and invalidate all the IOUSBHostDevice objects.

## Parameters

- `serviceQueue`: A serial queue that the app uses to service all the asynchronous requests it submits to the default control endpoint. By default the framework creates an internal serial queue for the client process.
- `completionHandler`: The block the framework calls after the client has successfully opened the USB accessory. The error parameter passed to the block is `nil` if the operation was successful. The framework invokes the block on an arbitrary thread.

## See Also

### Managing a USB accessory
- [func close(completionHandler: ((any Error)?) -> Void)](./close%28completionhandler%29.md)
  Closes all connections to the USB accessory for this process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory/open(servicequeue:completionhandler:))*