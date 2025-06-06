# KernelCompletion

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void KernelCompletion(OSAction * action, IOReturn status, const IOUserClientAsyncArgumentsArray asyncData, uint32_t asyncDataCount);
```

## See Also

- [AsyncCompletion](iouserclient/asynccompletion.md)
  Send asynchronous arguments to a completion supplied by ExternalMethod().
- [IOUserClientAsyncArgumentsArray](iouserclientasyncargumentsarray.md)
- [Arguments Array Maximum](3325601-arguments_array_maximum.md)
- [IOUserClientAsyncReferenceArray](iouserclientasyncreferencearray.md)
- [Reference Array Maximum](3325602-reference_array_maximum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/kernelcompletion)*