# direction

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The initial direction of the flow: incoming or outgoing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var direction: NETrafficDirection { get }
```

```objc
@property (readonly) NETrafficDirection direction;
```

## See Also

### Inspecting flow properties
- [var url: URL?](./url.md)
  The flow’s HTTP URL.
- [var identifier: UUID](./identifier.md)
  The unique identifier of the flow.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.
- [var NEFilterFlowBytesMax: UInt64](../nefilterflowbytesmax.md)
  The maximum number of bytes to pass or peek for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/direction)*