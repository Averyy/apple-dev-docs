# protocolFamily

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var protocolFamily: sa_family_t { get }
```

```objc
@property (readonly) sa_family_t protocolFamily;
```

## See Also

### Accessing packet properties
- [var data: Data](./data.md)
- [var metadata: NEFlowMetaData?](./metadata.md)
- [var direction: NETrafficDirection](./direction.md)
  The direction of the packet.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepacket/protocolfamily)*