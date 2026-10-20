# url

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The flow’s HTTP URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * URL;
```

#### Discussion

This parameter is only non-`nil` for flows that originate from WebKit browser objects.

## See Also

### Inspecting flow properties
- [var identifier: UUID](./identifier.md)
  The unique identifier of the flow.
- [var direction: NETrafficDirection](./direction.md)
  The initial direction of the flow: incoming or outgoing.
- [enum NETrafficDirection](../netrafficdirection.md)
  A type to represent the direction of network traffic.
- [var NEFilterFlowBytesMax: UInt64](../nefilterflowbytesmax.md)
  The maximum number of bytes to pass or peek for a flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/url)*