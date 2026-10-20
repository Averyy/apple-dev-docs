# IOUserClientMethodFunction

**Framework**: DriverKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
typedef int (*)(class OSObject *, void *, struct IOUserClientMethodArguments *) IOUserClientMethodFunction;
```

## See Also

### Responding to Messages
- [ExternalMethod](./iouserclient/externalmethod.md)
  Receive arguments from IOKit.framework IOConnectMethod calls.
- [IOUserClientMethodArguments](./iouserclientmethodarguments.md)
  Arguments to pass to IOConnectMethod calls.
- [IOUserClientMethodDispatch](./iouserclientmethoddispatch.md)
  A structure that specifies how to validate the arguments passed to a client method function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodfunction)*