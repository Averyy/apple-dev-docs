# IOUserClientMethodFunction

**Framework**: DriverKit  
**Kind**: typealias

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef int (*)(class OSObject *, void *, struct IOUserClientMethodArguments *) IOUserClientMethodFunction;
```

## See Also

- [ExternalMethod](iouserclient/externalmethod.md)
  Receive arguments from IOKit.framework IOConnectMethod calls.
- [IOUserClientMethodArguments](iouserclientmethodarguments.md)
  Arguments to pass to IOConnectMethod calls.
- [IOUserClientMethodDispatch](iouserclientmethoddispatch.md)
  A structure that specifies how to validate the arguments passed to a client method function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclientmethodfunction)*