# readData(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Read data from the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func readData(completionHandler: @escaping (Data?, (any Error)?) -> Void)
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

## Parameters

- `completionHandler`: A block that will be executed by the system on an internal system thread when some data is read from the flow. The block is passed either the data that was read or a non-nil error if an error occurred. See   in   for a list of possible errors. If the data parameter has a length of 0 then no data can be subsequently read from the flow.

## See Also

- [func write(Data, withCompletionHandler: ((any Error)?) -> Void)](neappproxytcpflow/write(_:withcompletionhandler:).md)
  Write data to the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/readdata(completionhandler:))*