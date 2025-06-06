# ExternalMethod

**Framework**: DriverKit  
**Kind**: method

Receive arguments from IOKit.framework IOConnectMethod calls.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t ExternalMethod(uint64_t selector, IOUserClientMethodArguments * arguments, const IOUserClientMethodDispatch * dispatch, OSObject * target, void * reference);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

IOConnectMethod calls from the owner of the connection come here. Any argument may be passed as NULL if not passed by the caller.

## Parameters

- `selector`: Selector argument to  .
- `arguments`: Structure describing all arguments being passed to  . See the   definition.
- `dispatch`: NULL when called in the driver. The    implementation may be called with a non-NULL argument to check   certain fields of the arguments structure before calling a target procedure   specified by the dispatch structure ‘function’ field, and the   ‘target’ and ‘reference’ parameters to this method.   See the   definition.
- `target`: Target for the dispatch function
- `reference`: Reference constant for the dispatch function

## See Also

- [IOUserClientMethodArguments](iouserclientmethodarguments.md)
  Arguments to pass to IOConnectMethod calls.
- [IOUserClientMethodDispatch](iouserclientmethoddispatch.md)
  A structure that specifies how to validate the arguments passed to a client method function.
- [IOUserClientMethodFunction](iouserclientmethodfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/externalmethod)*