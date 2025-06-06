# commitEditing(withDelegate:didCommit:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Attempts to commit any pending changes in known editors of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

Provides support for the NSEditor informal protocol. This method attempts to commit pending changes in known editors. Known editors are either instances of a subclass of `NSController` or (more rarely) user interface controls that may contain pending edits—such as text fields—that registered with the context using [`objectDidBeginEditing(_:)`](nscontroller/objectdidbeginediting(_:).md) and have not yet unregistered using a subsequent invocation of [`objectDidEndEditing(_:)`](nscontroller/objectdidendediting(_:).md).

The receiver iterates through the array of its known editors and invokes `commitEditing` on each. The receiver then sends the message specified by the `didCommitSelector` selector to the specified delegate.

The `didCommit` argument is the value returned by the editor specified by `editor` from the `commitEditing` message. The `contextInfo` argument is the same value specified as the `contextInfo` parameter—you may use this value however you wish.

If an error occurs while attempting to commit, for example if key-value coding validation fails, your implementation of this method should typically send the view in which editing is being performed a `presentError:modalForWindow:delegate:didRecoverSelector:contextInfo:` message, specifying the view’s containing window.

You may find this method useful in some situations (typically if you are using Cocoa Bindings) when you want to ensure that pending changes are applied before a change in user interface state. For example, you may need to ensure that changes pending in a text field are applied before a window is closed. See also [`commitEditing()`](nscontroller/commitediting().md) which performs a similar function but which allows you to handle any errors directly, although it provides no information beyond simple success/failure.

## Parameters

- `delegate`: An object that can serve as the receiver’s delegate. It should implement the method specified by  .
- `didCommitSelector`: A selector that is invoked on delegate. The method specified by the selector must have the same signature as the following method:
- `contextInfo`: Contextual information that is sent as the   argument to delegate when   is invoked.

## See Also

- [func objectDidBeginEditing(any NSEditor)](nscontroller/objectdidbeginediting(_:).md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](nscontroller/objectdidendediting(_:).md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Causes the receiver to attempt to commit any pending edits, returning [`true`](https://developer.apple.com/documentation/swift/true) if successful or no edits were pending.
- [func discardEditing()](nscontroller/discardediting.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/commitediting(withdelegate:didcommit:contextinfo:))*