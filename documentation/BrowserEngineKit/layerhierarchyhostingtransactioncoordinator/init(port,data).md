# init(port:data:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Creates a transaction coordinator using a Mach port reference and serialized data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(port: mach_port_t, data: Data) throws
```

```objc
+ (BELayerHierarchyHostingTransactionCoordinator *) coordinatorWithPort:(mach_port_t) port data:(NSData *) data error:(NSError **) error;
```

## Discussion

Use this initializer to reconstruct a transaction coordinator that your app serializes using [`encode(_:)`](./encode%28_%29.md) in another process.

This method takes ownership of the Mach port send right, even if an error occurs; don’t use or deallocate the port after calling this method.

## Parameters

- `port`: A Mach port (`mach_port_t`) that references the coordinator.
- `data`: The serialized data with which to reconstruct the coordinator.

## See Also

### Sharing a transaction coordinator using Mach
- [func encode((mach_port_t, Data) -> Void)](./encode%28_%29.md)
  Serializes the transaction coordinator into a Mach port reference and accompanying data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(port:data:))*