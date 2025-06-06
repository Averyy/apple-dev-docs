# handleInput(framer:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Notifies your protocol that new inbound data is available to parse.

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
func handleInput(framer: NWProtocolFramer.Instance) -> Int
```

## See Also

- [func handleOutput(framer: NWProtocolFramer.Instance, message: NWProtocolFramer.Message, messageLength: Int, isComplete: Bool)](nwprotocolframerimplementation/handleoutput(framer:message:messagelength:iscomplete:).md)
  Notifies your protocol about a new outbound message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframerimplementation/handleinput(framer:))*