# identifier

**Framework**: Network Extension  
**Kind**: property

The unique identifier of the flow.

**Availability**:
- iOS 13.1+
- iPadOS 13.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var identifier: UUID { get }
```

## See Also

- [var url: URL?](nefilterflow/url.md)
  The flow’s HTTP URL.
- [var direction: NETrafficDirection](nefilterflow/direction.md)
  The initial direction of the flow: incoming or outgoing.
- [enum NETrafficDirection](netrafficdirection.md)
  A type to represent the direction of network traffic.
- [var NEFilterFlowBytesMax: UInt64](nefilterflowbytesmax.md)
  The maximum number of bytes to pass or peek for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/identifier)*