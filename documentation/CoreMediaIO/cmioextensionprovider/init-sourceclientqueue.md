# init(source:clientQueue:)

**Framework**: Core Media I/O  
**Kind**: init

Creates an extension provider with the specified source and dispatch queue.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(source: any CMIOExtensionProviderSource, clientQueue: dispatch_queue_t?)
```

## Parameters

- `source`: An extension-specific object that conforms to the   protocol.
- `clientQueue`: A client dispatch queue, or   to use the default queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/init(source:clientqueue:))*