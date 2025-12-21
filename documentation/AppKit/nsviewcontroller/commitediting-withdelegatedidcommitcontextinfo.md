# commitEditing(withDelegate:didCommit:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Attempt to commit any currently edited results of the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

The receiver must have been registered as the editor of an object using [`objectDidBeginEditing:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/objectDidBeginEditing:), and has not yet been unregistered by a subsequent invocation of [`objectDidEndEditing:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/objectDidEndEditing:). When the committing has either succeeded or failed, send the `delegate` the message specified by `didCommitSelector`.

The `didCommitSelector` method must have the following method signature:.

```objc
- (void)editor:(id)editor didCommit:(BOOL)didCommit contextInfo:(void  *)contextInfo
```

If an error occurs while attempting to commit, for example if key-value coding validation fails, an implementation of this method should typically send the receiver’s view a[`presentError(_:modalFor:delegate:didPresent:contextInfo:)`](nsresponder/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md) message, specifying the view’s containing window.

You may find this method useful in some situations when you want to ensure that pending changes are applied before a change in user interface state. For example, you may need to ensure that changes pending in a text field are applied before a window is closed. See also [`commitEditing()`](nsviewcontroller/commitediting().md) which performs a similar function but which allows you to handle any errors directly, although it provides no information beyond simple success/failure.

## Parameters

- `delegate`: An object that can serve as the receiver’s delegate. It should implement the method specified by  .
- `didCommitSelector`: A selector that is invoked on delegate.
- `contextInfo`: Contextual information that is sent as the   argument to delegate when   is invoked.

## See Also

- [func commitEditing() -> Bool](nsviewcontroller/commitediting.md)
  Returns whether the receiver was able to commit any pending edits.
- [func discardEditing()](nsviewcontroller/discardediting.md)
  Causes the receiver to discard any changes, restoring the previous values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/commitediting(withdelegate:didcommit:contextinfo:))*