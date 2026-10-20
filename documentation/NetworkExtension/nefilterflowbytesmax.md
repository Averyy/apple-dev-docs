# NEFilterFlowBytesMax

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

The maximum number of bytes to pass or peek for a flow.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var NEFilterFlowBytesMax: UInt64 { get }
```

```c
#define NEFilterFlowBytesMax
```

#### Discussion

When used as a pass value, this value directs to flow to pass all upcoming bytes. When used as a peek value, it indicates the flow should peek as many bytes as possible.

## See Also

### Inspecting flow properties
- [var url: URL?](./nefilterflow/url.md)
  The flow’s HTTP URL.
- [var identifier: UUID](./nefilterflow/identifier.md)
  The unique identifier of the flow.
- [var direction: NETrafficDirection](./nefilterflow/direction.md)
  The initial direction of the flow: incoming or outgoing.
- [enum NETrafficDirection](./netrafficdirection.md)
  A type to represent the direction of network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflowbytesmax)*