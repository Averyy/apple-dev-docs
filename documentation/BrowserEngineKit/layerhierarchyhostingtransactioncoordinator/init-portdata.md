# init(port:data:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a transaction coordinator using a Mach port reference and serialized data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(port: mach_port_t, data: Data) throws
```

#### Discussion

Use this initializer to reconstruct a transaction coordinator that your app serializes using [`encode(_:)`](layerhierarchyhostingtransactioncoordinator/encode(_:).md) in another process.

This method takes ownership of the Mach port send right, even if an error occurs; don’t use or deallocate the port after calling this method.

## Parameters

- `port`: A Mach port (`mach_port_t`) that references the coordinator.
- `data`: The serialized data with which to reconstruct the coordinator.

## See Also

- [func encode((mach_port_t, Data) -> Void)](layerhierarchyhostingtransactioncoordinator/encode(_:).md)
  Serializes the transaction coordinator into a Mach port reference and accompanying data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(port:data:))*