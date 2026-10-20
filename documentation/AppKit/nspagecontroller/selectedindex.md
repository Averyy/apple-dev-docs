# selectedIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The currently selected object in the arranged objects array.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var selectedIndex: Int { get set }
```

```objc
@property NSInteger selectedIndex;
```

#### Discussion

To animate a transition to a new index, use the NSPageController class animator object.

This property is key-value observing compliant.

## See Also

### Page Controller Items
- [var arrangedObjects: [Any]](./arrangedobjects.md)
  An array containing the objects displayed in the page controller’s view.
- [func navigateForward(to: Any)](./navigateforward%28to%29.md)
  Navigates to the specific object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/selectedindex)*