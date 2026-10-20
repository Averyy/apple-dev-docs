# data

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
var data: Data { get }
```

```objc
@property (copy, readonly) NSData * data;
```

## See Also

### Accessing packet properties
- [var metadata: NEFlowMetaData?](./metadata.md)
- [var protocolFamily: sa_family_t](./protocolfamily.md)
- [var direction: NETrafficDirection](./direction.md)
  The direction of the packet.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepacket/data)*