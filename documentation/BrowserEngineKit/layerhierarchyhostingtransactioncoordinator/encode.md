# encode(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

passes a copy of the send right or `MACH_PORT_NULL` if inert. the receiver is responsible for disposing of `copiedPort`. the port and data should be consumed together and  once by `init(port:data:)`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func encode(_ block: (mach_port_t, Data) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/encode(_:))*