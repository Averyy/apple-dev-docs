# encode(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Encodes the coordinator into a `mach_port_t` send right and its accompanying metadata.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func encode(_ block: (mach_port_t, Data) -> Void)
```

#### Discussion

- The block is responsible for disposing of `copiedPort` - failure to manage its lifecycle will leak the port. Note that some functions (like `coordinatorWithPort:data:error:`) will assume control of the right for you.
- `copiedPort` will be `MACH_PORT_NULL` if the receiver is already invalidated.
- The port and data should ultimately be consumed together and  once by `coordinatorWithPort:data:error:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/encode(_:))*