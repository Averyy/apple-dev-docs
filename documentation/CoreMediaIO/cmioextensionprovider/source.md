# source

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The source for the provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
weak var source: (any CMIOExtensionProviderSource)? { get }
```

```objc
@property (atomic, weak, readonly) id<CMIOExtensionProviderSource> source;
```

## See Also

### Inspecting a Provider
- [var clientQueue: dispatch_queue_t](./clientqueue.md)
  The dispatch queue on which the system performs client operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/source)*