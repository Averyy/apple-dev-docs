# closeReadWithError(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Close the flow for further read operations.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func closeReadWithError(_ error: (any Error)?)
```

```objc
- (void) closeReadWithError:(NSError *) error;
```

## Mentions

- [Handling Flow Copying](../handling-flow-copying.md)

## Parameters

- `error`: An [`NSError`](../../Foundation/nserror.md) object indicating to the system the error that led to the closure. If the flow is not being closed due to an error, this parameter should be set to nil. See `NEAppProxyFlowError` below for a list of acceptable error codes.

## See Also

### Managing the flow life cycle
- [func open(withLocalEndpoint: NWHostEndpoint?, completionHandler: ((any Error)?) -> Void)](./open%28withlocalendpoint,completionhandler%29.md)
  Opens the flow, indicating to the system that the caller is ready to start receiving and sending data.
- [func closeWriteWithError((any Error)?)](./closewritewitherror%28_%29.md)
  Close the flow for further write operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/closereadwitherror(_:))*