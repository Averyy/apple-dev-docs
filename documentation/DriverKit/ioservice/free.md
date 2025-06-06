# free

**Framework**: DriverKit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void free();
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

Use this method to perform any final cleanup of your service, such as deallocating any memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](ioservice/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

- [init](ioservice/init.md)
  Handles the basic initialization of the service.
- [Start](ioservice/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](ioservice/stop.md)
  Stops the service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/free)*