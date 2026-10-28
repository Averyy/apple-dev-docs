# commitEditing(withDelegate:didCommit:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to commit any pending changes in known editors of the receiver.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) commitEditingWithDelegate:(id) delegate didCommitSelector:(SEL) didCommitSelector contextInfo:(void *) contextInfo;
```

## Discussion

Provides support for the NSEditor informal protocol. This method attempts to commit pending changes in known editors. Known editors are either instances of a subclass of `NSController` or (more rarely) user interface controls that may contain pending edits—such as text fields—that registered with the context using [`objectDidBeginEditing(_:)`](./objectdidbeginediting%28_%29.md) and have not yet unregistered using a subsequent invocation of [`objectDidEndEditing(_:)`](./objectdidendediting%28_%29.md).

The receiver iterates through the array of its known editors and invokes `commitEditing` on each. The receiver then sends the message specified by the `didCommitSelector` selector to the specified delegate.

The `didCommit` argument is the value returned by the editor specified by `editor` from the `commitEditing` message. The `contextInfo` argument is the same value specified as the `contextInfo` parameter—you may use this value however you wish.

If an error occurs while attempting to commit, for example if key-value coding validation fails, your implementation of this method should typically send the view in which editing is being performed a `presentError:modalForWindow:delegate:didRecoverSelector:contextInfo:` message, specifying the view’s containing window.

You may find this method useful in some situations (typically if you are using Cocoa Bindings) when you want to ensure that pending changes are applied before a change in user interface state. For example, you may need to ensure that changes pending in a text field are applied before a window is closed. See also [`commitEditing()`](./commitediting%28%29.md) which performs a similar function but which allows you to handle any errors directly, although it provides no information beyond simple success/failure.

## Parameters

- `delegate`: An object that can serve as the receiver’s delegate. It should implement the method specified by `didCommitSelector`.
- `didCommitSelector`: A selector that is invoked on delegate. The method specified by the selector must have the same signature as the following method:

  ```objc
  - (void)editor:(id)editor didCommit:(BOOL)didCommit contextInfo:(void  *)contextInfo
  ```
- `contextInfo`: Contextual information that is sent as the `contextInfo` argument to delegate when `didCommitSelector` is invoked.

## See Also

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](./objectdidbeginediting%28_%29.md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](./objectdidendediting%28_%29.md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](./commitediting%28%29.md)
  Attempts to commit any pending edits.
- [func discardEditing()](./discardediting%28%29.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/commitediting(withdelegate:didcommit:contextinfo:))*