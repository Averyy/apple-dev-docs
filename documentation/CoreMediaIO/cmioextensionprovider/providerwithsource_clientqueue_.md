# providerWithSource:clientQueue:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new extension provider with the specified source and dispatch queue.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) providerWithSource:(id<CMIOExtensionProviderSource>) source clientQueue:(dispatch_queue_t) clientQueue;
```

#### Return Value

A new extension provider.

## Parameters

- `source`: An extension-specific object that conforms to the [`CMIOExtensionProviderSource`](../cmioextensionprovidersource.md) protocol.
- `clientQueue`: A client dispatch queue, or `nil` to use the default queue.

## See Also

### Creating a Provider
- [init(source: any CMIOExtensionProviderSource, clientQueue: dispatch_queue_t?)](./init%28source,clientqueue%29.md)
  Creates an extension provider with the specified source and dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/providerwithsource:clientqueue:)*