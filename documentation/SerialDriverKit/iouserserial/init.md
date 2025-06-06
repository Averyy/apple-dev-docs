# init

**Framework**: SerialDriverKit  
**Kind**: method

Handles the basic initialization of the service.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
bool init();
```

#### Return Value

`YES` if initialization is successful, or `NO` if an error occurred.

#### Discussion

The system calls this method shortly after it instantiates your `IOUserSerial` subclass, and before it calls the [`Start`](iouserserial/start.md) method of your service. Override this method and use it to initialize your subclass. Limit the work you do in this method to simple tasks that must occur before your service starts. For example, use this method to allocate memory for your `ivars` structure.

Always call `super` at the beginning of your implementation of this method.

## See Also

- [Start](iouserserial/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserserial/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserserial/free.md)
  Performs any final cleanup for the service.
- [initWith](iouserserial/initwith.md)
  Initializes the private data structures associated with this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/init)*