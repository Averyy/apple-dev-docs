# KernelCompletion

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual void KernelCompletion(OSAction *action, IOReturn status, const IOUserClientAsyncArgumentsArray asyncData, uint32_t asyncDataCount);
```

## See Also

### Communicating with the Client
- [AsyncCompletion](./asynccompletion.md)
  Send asynchronous arguments to a completion supplied by ExternalMethod().
- [IOUserClientAsyncArgumentsArray](../iouserclientasyncargumentsarray.md)
- [Arguments Array Maximum](../api-3325601-arguments_array_maximum.md)
- [IOUserClientAsyncReferenceArray](../iouserclientasyncreferencearray.md)
- [Reference Array Maximum](../api-3325602-reference_array_maximum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/kernelcompletion)*