# parseOutput(minimumIncompleteLength:maximumLength:parse:)

**Framework**: Network  
**Kind**: method

Examines the content of output data while inside your output handler.

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
final func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool
```

#### Return Value

Returns true if the requested length was available to parse, or false if the conditions could not be met.

## Parameters

- `minimumIncompleteLength`: The minimum number of bytes that should be delivered to the parse completion.
- `maximumLength`: The maximum number of bytes that should be delivered to the parse completion.
- `parse`: A completion handler that will be called inline to examine a region of bytes. This will contain the buffer that matches the constraints, and a boolean indicating if this buffer represents the end of a message.

## See Also

- [func writeOutput(data: Data)](nwprotocolframer/instance/writeoutput(data:)-ydvk.md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func writeOutputNoCopy(length: Int) throws](nwprotocolframer/instance/writeoutputnocopy(length:).md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func passThroughOutput()](nwprotocolframer/instance/passthroughoutput.md)
  Indicates that your protocol no longer needs to handle output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:))*