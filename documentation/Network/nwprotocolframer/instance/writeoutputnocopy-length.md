# writeOutputNoCopy(length:)

**Framework**: Network  
**Kind**: method

Sends a specific number of bytes from a message while inside your output handler.

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
final func writeOutputNoCopy(length: Int) throws
```

## See Also

- [func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:).md)
  Examines the content of output data while inside your output handler.
- [func writeOutput(data: Data)](nwprotocolframer/instance/writeoutput(data:)-ydvk.md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func passThroughOutput()](nwprotocolframer/instance/passthroughoutput.md)
  Indicates that your protocol no longer needs to handle output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/writeoutputnocopy(length:))*