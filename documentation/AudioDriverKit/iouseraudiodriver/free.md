# free

**Framework**: AudioDriverKit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void free();
```

#### Discussion

Override this method inherited from [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService).

Use this method to perform any final cleanup of your service, such as deallocating any memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](iouseraudiodriver/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

- [init](iouseraudiodriver/init.md)
  Handles the basic initialization of the service.
- [Start](iouseraudiodriver/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouseraudiodriver/stop.md)
  Stops the service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/free)*