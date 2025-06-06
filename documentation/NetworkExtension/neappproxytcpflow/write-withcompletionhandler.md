# write(_:withCompletionHandler:)

**Framework**: Network Extension  
**Kind**: method

Write data to the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func write(_ data: Data) async throws
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

## Parameters

- `data`: An   object containing the data to write.
- `completionHandler`: A block that will be executed by the system on an internal system thread when the data is written into the receive buffer of the socket associated with the flow. The caller should use this callback as an indication that it is possible to write more data to the flow without using up excessive buffer memory. If an error occurs while writing the data then a non-nil   object is passed to the block. See   in   for a list of possible errors.

## See Also

- [func readData(completionHandler: (Data?, (any Error)?) -> Void)](neappproxytcpflow/readdata(completionhandler:).md)
  Read data from the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/write(_:withcompletionhandler:))*