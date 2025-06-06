# presentError(_:)

**Framework**: AppKit  
**Kind**: method

Presents an error alert to the user as a modal panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func presentError(_ error: any Error) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if error recovery was done; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method does not return until the user dismisses the alert and, if the error has recovery options and a recovery delegate, the error’s recovery delegate is sent an `attemptRecoveryFromError:optionIndex:` message.

The default `NSDocumentController` implementation of this method is equivalent to that of `NSResponder` while treating the application object as the next responder and forwarding error presentation messages to it. (The default `NSDocument` implementation of this method treats the shared `NSDocumentController` instance as the next responder and forwards these messages to it.) The default implementations of several `NSDocumentController` methods call this method.

The default implementation of this method calls [`willPresentError(_:)`](nsdocumentcontroller/willpresenterror(_:).md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](nsdocumentcontroller/willpresenterror(_:).md).

## Parameters

- `error`: An object containing the error to present.

## See Also

- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocumentcontroller/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](nsdocumentcontroller/willpresenterror(_:).md)
  Indicates an error condition and provides the opportunity to return the same or a different error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/presenterror(_:))*