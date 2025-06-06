# deliverInputNoCopy(length:message:isComplete:)

**Framework**: Network  
**Kind**: method

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

- [func parseInput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](nwprotocolframer/instance/parseinput(minimumincompletelength:maximumlength:parse:).md)
  Examines the content of input data while in your input handler.
- [func deliverInput(data: Data, message: NWProtocolFramer.Message, isComplete: Bool)](nwprotocolframer/instance/deliverinput(data:message:iscomplete:).md)
  Delivers an inbound message containing arbitrary data from your protocol to the application.
- [func passThroughInput()](nwprotocolframer/instance/passthroughinput.md)
  Indicates that your protocol no longer needs to handle input data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/deliverinputnocopy(length:message:iscomplete:))*