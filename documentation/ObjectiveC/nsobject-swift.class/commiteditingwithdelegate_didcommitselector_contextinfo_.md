# commitEditingWithDelegate:didCommitSelector:contextInfo:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Attempt to commit any currently edited results of the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) commitEditingWithDelegate:(id) delegate didCommitSelector:(SEL) didCommitSelector contextInfo:(void *) contextInfo;
```

## Discussion

The receiver must have been registered as the editor of an object using `objectDidBeginEditing:`, and has not yet been unregistered by a subsequent invocation of `objectDidEndEditing:`. When the committing has either succeeded or failed, send the following message to the specified object. The `didCommitSelector` method must have the following method signature:

```objc
- (void)editor:(id)editor didCommit:(BOOL)didCommit contextInfo:(void *)contextInfo
```

If an error occurs while attempting to commit, for example if key-value coding validation fails, an implementation of this method should typically send the NSView in which editing is being done a `presentError:modalForWindow:delegate:didRecoverSelector:contextInfo:` message, specifying the view’s containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate:didcommitselector:contextinfo:)*