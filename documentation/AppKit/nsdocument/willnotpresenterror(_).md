# willNotPresentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func willNotPresentError(_ error: any Error)
```

```objc
- (void) willNotPresentError:(NSError *) error;
```

## Discussion

Some `NSDocument` methods, like those involved in writing, may not immediately delete temporary files if there is a chance that the error can be recovered from and the operation can continue. To make sure that cleanup is always done, you should invoke this method with `NSDocument` errors that are not going to be passed to one of the `presentError:...` methods. For example, the `NSDocument` implementation of the `NSFilePresenter` method [`savePresentedItemChanges(completionHandler:)`](../../Foundation/nsfilepresenter/savepresenteditemchanges%28completionhandler%29.md) invokes this method when it invokes [`autosave(withImplicitCancellability:completionHandler:)`](./autosave%28withimplicitcancellability,completionhandler%29.md) and the completion handler is passed an `NSError` object, because it does not present the error to the user.

## Parameters

- `error`: An [`NSError`](../../Foundation/nserror.md) object returned by another `NSDocument` method.

## See Also

### Displaying Errors to the User
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.
- [func presentError(any Error) -> Bool](./presenterror%28_%29.md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](./willpresenterror%28_%29.md)
  Called when the receiver is about to present an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/willnotpresenterror(_:))*