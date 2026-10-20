# init(port:data:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Creates a layer hierarchy handle using a Mach port reference and serialized data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(port: mach_port_t, data: Data) throws
```

```objc
+ (BELayerHierarchyHandle *) handleWithPort:(mach_port_t) port data:(NSData *) data error:(NSError **) error;
```

#### Discussion

Use this initializer to reconstruct a layer hierarchy handle that your app serializes using [`encode(_:)`](./encode%28_%29.md) in another process.

This method takes ownership of the Mach port send right, even if an error occurs; don’t use or deallocate the port after calling this method.

## Parameters

- `port`: A Mach port (`mach_port_t`) that references the layer hierarchy.
- `data`: The serialized data with which to reconstruct the handle.

## See Also

### Sharing a layer hierarchy handle using Mach
- [func encode((mach_port_t, Data) -> Void)](./encode%28_%29.md)
  Serializes the hierarchy handle into a Mach port reference and accompanying data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/init(port:data:))*