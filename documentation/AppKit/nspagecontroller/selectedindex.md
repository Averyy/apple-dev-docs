# selectedIndex

**Framework**: AppKit  
**Kind**: property

The currently selected object in the arranged objects array.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var selectedIndex: Int { get set }
```

#### Discussion

To animate a transition to a new index, use the NSPageController class animator object.

This property is key-value observing compliant.

## See Also

- [var arrangedObjects: [Any]](nspagecontroller/arrangedobjects.md)
  An array containing the objects displayed in the page controller’s view.
- [func navigateForward(to: Any)](nspagecontroller/navigateforward(to:).md)
  Navigates to the specific object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/selectedindex)*