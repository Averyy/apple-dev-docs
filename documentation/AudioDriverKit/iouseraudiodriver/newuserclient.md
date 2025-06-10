# NewUserClient

**Framework**: AudioDriverKit  
**Kind**: method

Requests the creation of a new user client for the service.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t NewUserClient(uint32_t in_type, IOUserClient * * out_user_client);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method if your service supports communication though an external user client. When an app calls [`IOServiceOpen(_:_:_:_:)`](https://developer.apple.com/documentation/iokit/1514515-ioserviceopen) to start a new service, the system calls this method on the service passed to that function. In your implementation, call the [`Create`](https://developer.apple.com/documentation/DriverKit/IOService/Create) method to create a new [`IOUserClient`](https://developer.apple.com/documentation/DriverKit/IOUserClient) object for your service and return that object in the `userClient` parameter.

## Parameters

- `in_type`: The type passed to  .
- `out_user_client`: A pointer to a variable for returning the new user client object. Upon the successful creation of the user client object, assign it to this variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/newuserclient)*