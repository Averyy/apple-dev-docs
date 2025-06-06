# handler

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
var handler: ((NEFilterPacketContext, NWInterface, NETrafficDirection, UnsafeRawBufferPointer) -> NEFilterPacketProvider.Verdict)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterpacketprovider/handler)*