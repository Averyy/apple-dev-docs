# passThroughOutput()

**Framework**: Network  
**Kind**: method

Indicates that your protocol no longer needs to handle output data.

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
final func passThroughOutput()
```

## See Also

- [func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:).md)
  Examines the content of output data while inside your output handler.
- [func writeOutput(data: Data)](nwprotocolframer/instance/writeoutput(data:)-ydvk.md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func writeOutputNoCopy(length: Int) throws](nwprotocolframer/instance/writeoutputnocopy(length:).md)
  Sends a specific number of bytes from a message while inside your output handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/passthroughoutput())*