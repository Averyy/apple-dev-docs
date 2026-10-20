# state

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The state of the menu item.

**Availability**:
- macOS

## Declaration

```swift
var state: NSControl.StateValue { get set }
```

```objc
@property NSControlStateValue state;
```

#### Discussion

The image associated with the new state is displayed to the left of the menu item.

## See Also

### Related Documentation
- [var offStateImage: NSImage?](./offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](./mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [var onStateImage: NSImage!](./onstateimage.md)
  The image of the menu item that indicates an “on” state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/state)*