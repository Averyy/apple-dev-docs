# deliverInputNoCopy(length:message:isComplete:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Delivers an inbound message containing a specific number of next received bytes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final func deliverInputNoCopy(length: Int, message: NWProtocolFramer.Message, isComplete: Bool) -> Bool
```

## See Also

### Delivering Input
- [func parseInput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](./parseinput%28minimumincompletelength,maximumlength,parse%29.md)
  Examines the content of input data while in your input handler.
- [func deliverInput(data: Data, message: NWProtocolFramer.Message, isComplete: Bool)](./deliverinput%28data,message,iscomplete%29.md)
  Delivers an inbound message containing arbitrary data from your protocol to the application.
- [func passThroughInput()](./passthroughinput%28%29.md)
  Indicates that your protocol no longer needs to handle input data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/deliverinputnocopy(length:message:iscomplete:))*