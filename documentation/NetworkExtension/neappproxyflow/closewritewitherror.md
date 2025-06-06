# closeWriteWithError(_:)

**Framework**: Network Extension  
**Kind**: method

Close the flow for further write operations.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func closeWriteWithError(_ error: (any Error)?)
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

## Parameters

- `error`: An NSError object indicating to the system the error that led to the closure. If the flow is not being closed due to an error, this parameter should be set to nil. See   below for a list of acceptable error codes.

## See Also

- [func open(withLocalEndpoint: NWHostEndpoint?, completionHandler: ((any Error)?) -> Void)](neappproxyflow/open(withlocalendpoint:completionhandler:).md)
  Opens the flow, indicating to the system that the caller is ready to start receiving and sending data.
- [func closeReadWithError((any Error)?)](neappproxyflow/closereadwitherror(_:).md)
  Close the flow for further read operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/closewritewitherror(_:))*