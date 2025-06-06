# AsyncCompletion

**Framework**: DriverKit  
**Kind**: method

Send asynchronous arguments to a completion supplied by ExternalMethod().

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void AsyncCompletion(OSAction * action, IOReturn status, const IOUserClientAsyncArgumentsArray asyncData, uint32_t asyncDataCount);
```

#### Discussion

IOConnectAsyncMethod calls from the owner of the connection come will pass an OSAction instance. To deliver the asynchronous results the driver calls AsyncCompletion().

## Parameters

- `action`: OSAction passed to IOExternalMethod().
- `status`: An IOReturn status value to be sent.
- `asyncData`: An array of scalar data to be sent.
- `asyncDataCount`: Count of valid data in asyncData.

## See Also

- [KernelCompletion](iouserclient/kernelcompletion.md)
- [IOUserClientAsyncArgumentsArray](iouserclientasyncargumentsarray.md)
- [Arguments Array Maximum](3325601-arguments_array_maximum.md)
- [IOUserClientAsyncReferenceArray](iouserclientasyncreferencearray.md)
- [Reference Array Maximum](3325602-reference_array_maximum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/asynccompletion)*