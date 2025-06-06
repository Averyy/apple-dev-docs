# NewUserClient

**Framework**: DriverKit  
**Kind**: method

Requests the creation of a new user client for the service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t NewUserClient(uint32_t type, IOUserClient * * userClient);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

Override this method if your service supports communication though an external user client. When an app calls [`IOServiceOpen(_:_:_:_:)`](https://developer.apple.com/documentation/iokit/1514515-ioserviceopen) to start a new service, the system calls this method on the service passed to that function. In your implementation, call the [`Create`](ioservice/create.md) method to create a new [`IOUserClient`](iouserclient.md) object for your service and return that object in the `userClient` parameter.

## Parameters

- `type`: The type passed to  .
- `userClient`: A pointer to a variable for returning the new user client object. Upon the successful creation of the user client object, assign it to this variable.

## See Also

- [Create](ioservice/create.md)
  Requests the creation of a new service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/newuserclient)*