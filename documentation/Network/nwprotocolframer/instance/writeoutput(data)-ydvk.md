# writeOutput(data:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Sends arbitrary output data from your protocol to the next protocol.

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
final func writeOutput(data: Data)
```

## See Also

### Writing Output
- [func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](./parseoutput%28minimumincompletelength,maximumlength,parse%29.md)
  Examines the content of output data while inside your output handler.
- [func writeOutputNoCopy(length: Int) throws](./writeoutputnocopy%28length%29.md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func passThroughOutput()](./passthroughoutput%28%29.md)
  Indicates that your protocol no longer needs to handle output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/writeoutput(data:)-ydvk)*