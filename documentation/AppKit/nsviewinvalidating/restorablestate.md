# restorableState

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A change that invalidates the restorable state of the view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
static var restorableState: NSView.Invalidations.RestorableState { get }
```

#### Discussion

Use this invalidation type to call [`invalidateRestorableState()`](../nsresponder/invalidaterestorablestate%28%29.md) so that a change in property value invalidates the viewʼs restorable state. This triggers the app to save any information the restoration system needs to restore the current state of the view.

## See Also

### Creating the invalidation type
- [init()](../nsview/invalidations/restorablestate/init%28%29.md)
  Creates the invalidation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating/restorablestate)*