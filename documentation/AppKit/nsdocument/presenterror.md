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

[`true`](https://developer.apple.com/documentation/swift/true) if error recovery was done; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method does not return until the user dismisses the alert and, if the error has recovery options and a recovery delegate, the error’s recovery delegate  is sent an doc://com.apple.documentation/documentation/objectivec/nsobject/1416402-attemptrecovery message.

The `NSDocument` default implementation of this method is equivalent to that of `NSResponder` and treats the shared `NSDocumentController` as the next responder and forwards these messages to it.

The default implementation of this method invokes [`willPresentError(_:)`](nsdocument/willpresenterror(_:).md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](nsdocument/willpresenterror(_:).md).

## Parameters

- `error`: The error object encapsulating the information to present to the user.

## See Also

- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](nsdocument/willpresenterror(_:).md)
  Called when the receiver is about to present an error.
- [func willNotPresentError(any Error)](nsdocument/willnotpresenterror(_:).md)
  Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/presenterror(_:))*