# free

**Framework**: SerialDriverKit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void free();
```

#### Discussion

Use this method to deallocate the memory associated with your service, or perform other cleanup tasks. The system calls this method at some point after it calls your service’s [`Stop`](iouserserial/stop.md) method.

Always call `super` at the end of your implementation of this method.

## See Also

- [init](iouserserial/init.md)
  Handles the basic initialization of the service.
- [Start](iouserserial/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserserial/stop.md)
  Stops the service associated with the specified provider.
- [initWith](iouserserial/initwith.md)
  Initializes the private data structures associated with this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/free)*