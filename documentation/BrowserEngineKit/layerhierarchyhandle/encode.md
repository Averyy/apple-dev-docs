# encode(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Encodes the handle into a `mach_port_t` send right and its accompanying metadata.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func encode(_ block: (mach_port_t, Data) -> Void)
```

#### Discussion

- The block is responsible for disposing of `copiedPort` - failure to manage its lifecycle will leak the port. Note that some functions (like `handleWithPort:data:error:`) will assume control of the right for you.
- `copiedPort` will be `MACH_PORT_NULL` if the [`LayerHierarchy`](layerhierarchy.md) pointed to by the handle is already invalidated.
- The port and data should ultimately be consumed together  by `handleWithPort:data:error:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/encode(_:))*