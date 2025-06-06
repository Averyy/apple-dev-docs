# initWith

**Framework**: SerialDriverKit  
**Kind**: method

Initializes the private data structures associated with this class.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
bool initWith(IOBufferMemoryDescriptor * ifmd);
```

#### Return Value

`YES` if initialization succeeded, or `NO` if it didn’t.

#### Discussion

Do not override or call this method. Instead, override the [`init`](https://developer.apple.com/documentation/USBSerialDriverKit/IOUserUSBSerial/init) method and use it to allocate memory for your driver’s data structures.

## Parameters

- `ifmd`: The memory buffer to use for interrupt-related data.

## See Also

- [init](iouserserial/init.md)
  Handles the basic initialization of the service.
- [Start](iouserserial/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserserial/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserserial/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/initwith)*