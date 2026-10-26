# initWithIOService:queue:error:interestHandler:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Creates a USB host object and sets up a default communication channel to the kernel.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (instancetype) initWithIOService:(io_service_t) ioService queue:(dispatch_queue_t) queue error:(NSError **) error interestHandler:(IOUSBHostInterestHandler) interestHandler;
```

#### Return Value

An [`IOUSBHostObject`](../iousbhostobject.md) instance, or `nil` on failure.

#### Discussion

If the kernel [`IOUSBHostDevice`](../../kernel/iousbhostdevice.md) or [`IOUSBHostInterface`](../iousbhostinterface.md) is already open for exclusive access, the method returns `nil`. The method establishes exclusive ownership of the [`io_service_t`](../../kernel/io_service_t.md).

> ❗ **Important**:  When done with the object, call [`destroy()`](./destroy%28%29.md).

## Parameters

- `ioService`: The service type of the [`IOUSBHostDevice`](../../kernel/iousbhostdevice.md) or [`IOUSBHostInterface`](../../kernel/iousbhostinterface.md). The [`IOUSBHostObject`](../iousbhostobject.md) keeps a reference to the service type and releases it during [`destroy()`](./destroy%28%29.md).
- `queue`: A serial dispatch queue for servicable asynchronous input/output requests. By default, this method creates a serial queue on behalf of the client.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.
- `interestHandler`: A callback for managing internal device state changes, such as termination.

## Topics

### Interest Handler
- [typealias IOUSBHostInterestHandler](../iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.

## See Also

### Managing the Object Life Cycle
- [struct IOUSBHostObjectInitOptions](../iousbhostobjectinitoptions.md)
  Options for initializing the host object.
- [- initWithIOService:options:queue:error:interestHandler:](./initwithioservice_options_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a communication channel to the kernel.
- [typealias IOUSBHostInterestHandler](../iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](./ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](./queue.md)
  The queue for servicing input/output requests.
- [func destroy()](./destroy%28%29.md)
  Removes underlying allocations and connections from the USB host object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/initwithioservice:queue:error:interesthandler:)*