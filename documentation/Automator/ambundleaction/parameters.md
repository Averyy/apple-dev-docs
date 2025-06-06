# parameters

**Framework**: Automator  
**Kind**: property

The action’s parameters.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var parameters: NSMutableDictionary? { get set }
```

#### Discussion

The parameters of an action reflect the choices made and values entered in the action’s user interface. Keys in the parameters dictionary identify specific user-interface objects. If an action uses the Cocoa bindings mechanism, the parameters of an [`AMBundleAction`](ambundleaction.md) object are automatically set.

## See Also

- [var bundle: Bundle](ambundleaction/bundle.md)
  The action’s bundle object.
- [var hasView: Bool](ambundleaction/hasview.md)
  A Boolean value that indicates whether the action has a view associated with it.
- [var view: NSView?](ambundleaction/view.md)
  The action’s view object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/ambundleaction/parameters)*