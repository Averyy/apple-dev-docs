# IOUserClient

**Framework**: DriverKit  
**Kind**: class

A connection to another service that the system manages.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOUserClient;
```

#### Overview

An application may open an IOUserClient by calling IOServiceOpen(). This results in a call to the IOService::NewUserClient API to create an instance representing the connection. and to receive untyped data via IOConnectMethod/IOConnectAsyncMethod. As an IOService subclass, IOUserClient receives the normal Start()/Stop() lifecyle calls.

## Topics

### Configuring a User Client
- [init](iouserclient/init.md)
- [free](iouserclient/free.md)
### Communicating with the Client
- [AsyncCompletion](iouserclient/asynccompletion.md)
  Send asynchronous arguments to a completion supplied by ExternalMethod().
- [KernelCompletion](iouserclient/kernelcompletion.md)
- [IOUserClientAsyncArgumentsArray](iouserclientasyncargumentsarray.md)
- [Arguments Array Maximum](3325601-arguments_array_maximum.md)
- [IOUserClientAsyncReferenceArray](iouserclientasyncreferencearray.md)
- [Reference Array Maximum](3325602-reference_array_maximum.md)
### Responding to Messages
- [ExternalMethod](iouserclient/externalmethod.md)
  Receive arguments from IOKit.framework IOConnectMethod calls.
- [IOUserClientMethodArguments](iouserclientmethodarguments.md)
  Arguments to pass to IOConnectMethod calls.
- [IOUserClientMethodDispatch](iouserclientmethoddispatch.md)
  A structure that specifies how to validate the arguments passed to a client method function.
- [IOUserClientMethodFunction](iouserclientmethodfunction.md)
### Mapping to the Client’s Memory Space
- [CopyClientMemoryForType](iouserclient/copyclientmemoryfortype.md)
  Return an IOMemoryDescriptor to be mapped into the client task.
- [Copy Client Memory Options](3325603-copy_client_memory_options.md)
### Instance Methods
- [CopyClientEntitlements](iouserclient/copycliententitlements.md)
- [CreateMemoryDescriptorFromClient](iouserclient/creatememorydescriptorfromclient.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOUserServer](iouserserver.md)
  A system-managed service.
- [com.apple.developer.driverkit.userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [Communicating between a DriverKit extension and a client app](communicating-between-a-driverkit-extension-and-a-client-app.md)
  Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient)*