# presentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents an error alert to the user as an application-modal dialog.

**Availability**:
- macOS

## Declaration

```swift
func presentError(_ error: any Error) -> Bool
```

```objc
- (BOOL) presentError:(NSError *) error;
```

#### Discussion

The alert displays information found in the [`NSError`](../../Foundation/nserror.md) object `error`; this information can include error description, recovery suggestion, failure reason, and button titles (all localized). The method returns [`true`](../../Swift/true.md) if error recovery succeeded and [`false`](../../Swift/false.md) otherwise. For error recovery to be attempted, an recovery-attempter object (that is, an object conforming to the `NSErrorRecoveryAttempting` informal protocol) must be associated with `error`.

The default implementation of this method sends [`willPresentError(_:)`](./willpresenterror%28_%29.md) to `self`. By doing this, `NSResponder` gives subclasses an opportunity to customize error presentation. It then forwards the message, passing any customized error object, to the next responder; if there is no next responder, it passes the error object to `NSApp`, which displays a document-modal error alert. When the user dismisses the alert, any recovery attempter associated with the error object is given a chance to recover from the error. See the class description for the precise route up the responder chain (plus document and controller objects) this message might travel.

It is not recommended that you attempt to override this method. If you wish to customize the error presentation, override [`willPresentError(_:)`](./willpresenterror%28_%29.md) instead.

## Parameters

- `error`: An object containing information about an error.

## See Also

### Presenting and Customizing Error Information
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a document-modal sheet attached to document window.
- [func willPresentError(any Error) -> any Error](./willpresenterror%28_%29.md)
  Returns a custom version of the supplied error object that’s more suitable for presentation in alert sheets and dialogs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/presenterror(_:))*