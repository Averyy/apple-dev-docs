# parameters

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

The action’s parameters.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var parameters: NSMutableDictionary? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSMutableDictionary<NSString *,id> * parameters;
```

#### Discussion

The parameters of an action reflect the choices made and values entered in the action’s user interface. Keys in the parameters dictionary identify specific user-interface objects. If an action uses the Cocoa bindings mechanism, the parameters of an [`AMBundleAction`](../ambundleaction.md) object are automatically set.

## See Also

### Managing Action Properties
- [var bundle: Bundle](./bundle.md)
  The action’s bundle object.
- [var hasView: Bool](./hasview.md)
  A Boolean value that indicates whether the action has a view associated with it.
- [var view: NSView?](./view.md)
  The action’s view object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/ambundleaction/parameters)*