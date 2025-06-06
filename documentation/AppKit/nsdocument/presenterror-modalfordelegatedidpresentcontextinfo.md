# presentError(_:modalFor:delegate:didPresent:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Presents an error alert to the user as a modal panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func presentError(_ error: any Error, modalFor window: NSWindow, delegate: Any?, didPresent didPresentSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

When the user dismisses the alert and any recovery possible for the error and chosen by the user has been attempted, sends the message `didPresentSelector` to the specified `delegate`.

The `NSDocument` default implementation of this method is equivalent to that of `NSResponder` and treats the shared `NSDocumentController` object as the next responder and forwards these messages to it. The default implementations of several `NSDocument` methods invoke this method.

The default implementation of this method invokes [`willPresentError(_:)`](nsdocument/willpresenterror(_:).md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](nsdocument/willpresenterror(_:).md).

The method selected by `didPresentSelector` must have the same signature as:

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover contextInfo:(void  *)contextInfo
```

## Parameters

- `error`: The error object encapsulating the information to present to the user.
- `window`: The window to which the modal alert belongs.
- `delegate`: The delegate to which the selector message is sent.
- `didPresentSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [func presentError(any Error) -> Bool](nsdocument/presenterror(_:).md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](nsdocument/willpresenterror(_:).md)
  Called when the receiver is about to present an error.
- [func willNotPresentError(any Error)](nsdocument/willnotpresenterror(_:).md)
  Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/presenterror(_:modalfor:delegate:didpresent:contextinfo:))*