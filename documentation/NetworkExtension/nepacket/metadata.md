# metadata

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var metadata: NEFlowMetaData? { get }
```

```objc
@property (readonly, nullable) NEFlowMetaData * metadata;
```

## See Also

### Accessing packet properties
- [var data: Data](./data.md)
- [var protocolFamily: sa_family_t](./protocolfamily.md)
- [var direction: NETrafficDirection](./direction.md)
  The direction of the packet.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepacket/metadata)*