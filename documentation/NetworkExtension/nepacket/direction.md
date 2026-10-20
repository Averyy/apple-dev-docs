# direction

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The direction of the packet.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var direction: NETrafficDirection { get }
```

```objc
@property (readonly) NETrafficDirection direction;
```

## See Also

### Accessing packet properties
- [var data: Data](./data.md)
- [var metadata: NEFlowMetaData?](./metadata.md)
- [var protocolFamily: sa_family_t](./protocolfamily.md)
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepacket/direction)*