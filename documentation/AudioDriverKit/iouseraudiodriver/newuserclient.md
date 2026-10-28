# NewUserClient

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Requests the creation of a new user client for the service.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t NewUserClient(uint32_t in_type, IOUserClient **out_user_client);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Override this method if your service supports communication though an external user client. When an app calls [`IOServiceOpen(_:_:_:_:)`](../../iokit/api-1514515-ioserviceopen.md) to start a new service, the system calls this method on the service passed to that function. In your implementation, call the [`Create`](../../DriverKit/ioservice/create.md) method to create a new [`IOUserClient`](../../DriverKit/iouserclient.md) object for your service and return that object in the `userClient` parameter.

## Parameters

- `in_type`: The type passed to [`IOServiceOpen(_:_:_:_:)`](../../iokit/api-1514515-ioserviceopen.md).
- `out_user_client`: A pointer to a variable for returning the new user client object. Upon the successful creation of the user client object, assign it to this variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/newuserclient)*