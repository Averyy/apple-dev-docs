# presentError(_:)

**Framework**: AppKit  
**Kind**: method

Presents an error alert to the user as an application-modal dialog.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func presentError(_ error: any Error) -> Bool
```

#### Discussion

The alert displays information found in the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object `error`; this information can include error description, recovery suggestion, failure reason, and button titles (all localized). The method returns [`true`](https://developer.apple.com/documentation/Swift/true) if error recovery succeeded and [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. For error recovery to be attempted, an recovery-attempter object (that is, an object conforming to the `NSErrorRecoveryAttempting` informal protocol) must be associated with `error`.

The default implementation of this method sends [`willPresentError(_:)`](nsresponder/willpresenterror(_:).md) to `self`. By doing this, `NSResponder` gives subclasses an opportunity to customize error presentation. It then forwards the message, passing any customized error object, to the next responder; if there is no next responder, it passes the error object to `NSApp`, which displays a document-modal error alert. When the user dismisses the alert, any recovery attempter associated with the error object is given a chance to recover from the error. See the class description for the precise route up the responder chain (plus document and controller objects) this message might travel.

It is not recommended that you attempt to override this method. If you wish to customize the error presentation, override [`willPresentError(_:)`](nsresponder/willpresenterror(_:).md) instead.

## Parameters

- `error`: An object containing information about an error.

## See Also

- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsresponder/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md)
  Presents an error alert to the user as a document-modal sheet attached to document window.
- [func willPresentError(any Error) -> any Error](nsresponder/willpresenterror(_:).md)
  Returns a custom version of the supplied error object that’s more suitable for presentation in alert sheets and dialogs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/presenterror(_:))*