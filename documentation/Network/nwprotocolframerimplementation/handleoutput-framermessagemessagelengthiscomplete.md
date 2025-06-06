# handleOutput(framer:message:messageLength:isComplete:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Notifies your protocol about a new outbound message.

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
func handleOutput(framer: NWProtocolFramer.Instance, message: NWProtocolFramer.Message, messageLength: Int, isComplete: Bool)
```

#### Discussion

The output handler is your opportunity to encapsulate or encode a signle application message. You should write any output using [`writeOutput(data:)`](nwprotocolframer/instance/writeoutput(data:)-ydvk.md) or [`writeOutputNoCopy(length:)`](nwprotocolframer/instance/writeoutputnocopy(length:).md) before returning from the output handler. If you do not write a message, the application message will be discarded.

## Parameters

- `framer`: The framer instance associated with the connection.
- `message`: The framer message passed by the application.
- `messageLength`: The length of the message content being sent.
- `isComplete`: A boolean indicating if this the last chunk of a message.

## See Also

- [func handleInput(framer: NWProtocolFramer.Instance) -> Int](nwprotocolframerimplementation/handleinput(framer:).md)
  Notifies your protocol that new inbound data is available to parse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframerimplementation/handleoutput(framer:message:messagelength:iscomplete:))*