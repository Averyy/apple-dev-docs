# presentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents an error alert to the user as a modal panel.

**Availability**:
- macOS

## Declaration

```swift
func presentError(_ error: any Error) -> Bool
```

```objc
- (BOOL) presentError:(NSError *) error;
```

#### Return Value

[`true`](../../Swift/true.md) if error recovery was done; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method does not return until the user dismisses the alert and, if the error has recovery options and a recovery delegate, the error’s recovery delegate  is sent an [`attemptRecovery(fromError:optionIndex:)`](../../ObjectiveC/nsobject-swift.class/attemptrecovery%28fromerror,optionindex%29.md) message.

The `NSDocument` default implementation of this method is equivalent to that of `NSResponder` and treats the shared `NSDocumentController` as the next responder and forwards these messages to it.

The default implementation of this method invokes [`willPresentError(_:)`](./willpresenterror%28_%29.md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](./willpresenterror%28_%29.md).

## Parameters

- `error`: The error object encapsulating the information to present to the user.

## See Also

### Displaying Errors to the User
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](./willpresenterror%28_%29.md)
  Called when the receiver is about to present an error.
- [func willNotPresentError(any Error)](./willnotpresenterror%28_%29.md)
  Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/presenterror(_:))*