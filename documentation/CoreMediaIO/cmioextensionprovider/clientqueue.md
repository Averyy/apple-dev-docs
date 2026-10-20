# clientQueue

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which the system performs client operations.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var clientQueue: dispatch_queue_t { get }
```

```objc
@property (atomic, strong, readonly) dispatch_queue_t clientQueue;
```

## See Also

### Inspecting a Provider
- [var source: (any CMIOExtensionProviderSource)?](./source.md)
  The source for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/clientqueue)*